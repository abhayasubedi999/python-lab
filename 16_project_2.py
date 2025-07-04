import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
import json
import datetime
from typing import List, Dict, Optional
from urllib.parse import urljoin

DB_NAME = "news.db"


class NewsDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                url TEXT,
                is_active BOOLEAN DEFAULT 1
            )
        """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_id INTEGER,
                title TEXT,
                content TEXT,
                url TEXT,
                published_at TEXT,
                scraped_at TEXT,
                FOREIGN KEY (source_id) REFERENCES sources(id)
            )
        """
        )
        self.conn.commit()

    def add_source(self, name: str, url: str):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO sources (name, url) VALUES (?, ?)", (name, url))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Source '{name}' already exists!")
            return False

    def delete_source(self, name: str):
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM news WHERE source_id IN (SELECT id FROM sources WHERE name = ?)",
            (name,),
        )
        cursor.execute("UPDATE sources SET is_active = 0 WHERE name = ?", (name,))
        print(f"News Source '{name}' marked inactive and news deleted.")
        self.conn.commit()
        return cursor.rowcount > 0

    def get_active_sources(self) -> List[Dict]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, url FROM sources WHERE is_active = 1")
        return [
            {"id": row[0], "name": row[1], "url": row[2]} for row in cursor.fetchall()
        ]

    def save_news(
        self, source_id: int, title: str, content: str, url: str, published_at: str
    ):
        if not title:
            return  # Skip empty title
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO news (source_id, title, content, url, published_at, scraped_at)
            VALUES (?, ?, ?, ?, ?, datetime('now'))
        """,
            (source_id, title, content, url, published_at),
        )
        self.conn.commit()

    def get_news_by_date_and_source(
        self, date: str, source_name: Optional[str] = None
    ) -> List[Dict]:
        cursor = self.conn.cursor()
        query = """
            SELECT n.title, n.content, n.url, n.published_at, s.name as source
            FROM news n
            JOIN sources s ON n.source_id = s.id
            WHERE date(n.scraped_at) = ?
        """
        params = [date]
        if source_name:
            query += " AND s.name = ?"
            params.append(source_name)
        cursor.execute(query, params)
        return [
            {
                "title": row[0],
                "content": row[1],
                "url": row[2],
                "published_at": row[3],
                "source": row[4],
            }
            for row in cursor.fetchall()
        ]


class NewsScraper:
    @staticmethod
    def scrape_generic(url: str, selectors: Dict) -> List[Dict]:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            news_items = []
            for article in soup.select(selectors["container"]):
                title_tag = article.select_one(selectors["title"])
                title = title_tag.text.strip() if title_tag else ""
                content_tag = article.select_one(selectors["content"])
                content = content_tag.text.strip() if content_tag else ""
                link_tag = article.select_one(selectors["title"])
                news_url = (
                    urljoin(url, link_tag["href"])
                    if link_tag and link_tag.has_attr("href")
                    else ""
                )
                time_tag = article.select_one(selectors.get("time", ""))
                published_at = (
                    time_tag.text.strip()
                    if time_tag
                    else datetime.date.today().strftime("%Y-%m-%d")
                )
                if title:
                    news_items.append(
                        {
                            "title": title,
                            "content": content,
                            "url": news_url,
                            "published_at": published_at,
                        }
                    )
            return news_items
        except Exception as e:
            print(f"Error scraping: {e}")
            return []

    @staticmethod
    def scrape_news(source_name: str, url: str) -> List[Dict]:
        source_name_lower = source_name.lower()
        if "ratopati" in source_name_lower:
            return NewsScraper.scrape_generic(
                url,
                {
                    "container": ".news-list-item",
                    "title": ".news-title a",
                    "content": ".news-excerpt",
                    "time": ".time",
                },
            )
        elif "ekantipur" in source_name_lower:
            return NewsScraper.scrape_generic(
                url,
                {
                    "container": ".normal",
                    "title": "h2 a",
                    "content": "p",
                    "time": ".time",
                },
            )
        elif "annapurna" in source_name_lower:
            return NewsScraper.scrape_generic(
                url,
                {
                    "container": ".news-item",
                    "title": "h3 a",
                    "content": "p",
                    "time": ".time",
                },
            )
        else:
            return NewsScraper.scrape_generic(
                url,
                {"container": "article", "title": "h2", "content": "p", "time": "time"},
            )


class NewsManager:
    def __init__(self):
        self.db = NewsDatabase()
        self.initialize_default_sources()

    def initialize_default_sources(self):
        default_sources = [
            {"name": "Ratopati", "url": "https://www.ratopati.com/"},
            {"name": "Ekantipur", "url": "https://ekantipur.com/"},
            {"name": "Annapurna Post", "url": "https://www.annapurnapost.com/"},
        ]
        for source in default_sources:
            self.db.add_source(source["name"], source["url"])

    def add_source(self, name: str, url: str):
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        return self.db.add_source(name, url)

    def delete_source(self, name: str):
        return self.db.delete_source(name)

    def load_news(self):
        sources = self.db.get_active_sources()
        for source in sources:
            print(f"Scraping news from {source['name']}...")
            news_items = NewsScraper.scrape_news(source["name"], source["url"])
            for item in news_items:
                self.db.save_news(
                    source["id"],
                    item["title"],
                    item["content"],
                    item["url"],
                    item["published_at"],
                )
            print(f"Added {len(news_items)} news items from {source['name']}")

    def dump_news_to_csv(self, date: str, source_name: Optional[str] = None):
        news_items = self.db.get_news_by_date_and_source(date, source_name)
        filename = f"{date.replace('-', '')}_{(source_name.lower() if source_name else 'all')}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=["title", "content", "url", "published_at", "source"],
            )
            writer.writeheader()
            writer.writerows(news_items)
        print(f"Saved {len(news_items)} news items to {filename}")

    def dump_news_to_json(self, date: str, source_name: Optional[str] = None):
        news_items = self.db.get_news_by_date_and_source(date, source_name)
        filename = f"{date.replace('-', '')}_{(source_name.lower() if source_name else 'all')}.json"
        with open(filename, "w", encoding="utf-8") as jsonfile:
            json.dump(news_items, jsonfile, ensure_ascii=False, indent=2)
        print(f"Saved {len(news_items)} news items to {filename}")


def get_user_choice():
    return input(
        """
Samachar Sangraha
1. Add news source
2. Delete news source
3. Load news
4. Dump news CSV
5. Dump news JSON
6. Exit
Choice: """
    )


def main():
    manager = NewsManager()
    while True:
        choice = get_user_choice()
        if choice == "6":
            break
        elif choice == "1":
            name = input("Source name: ")
            url = input("Source URL: ")
            manager.add_source(name, url)
        elif choice == "2":
            name = input("Source name to delete: ")
            manager.delete_source(name)
        elif choice == "3":
            manager.load_news()
        elif choice == "4":
            date = input("Date YYYY-MM-DD: ")
            source = input("Source (optional): ")
            manager.dump_news_to_csv(date, source or None)
        elif choice == "5":
            date = input("Date YYYY-MM-DD: ")
            source = input("Source (optional): ")
            manager.dump_news_to_json(date, source or None)
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
