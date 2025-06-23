# Create a Hangman with user option to choose level. There has to be level as Easy, Difficult and Hard. Words for this game taken from json file that has words separated on the basis of level. If user is able to guess word in 5 attempt display You Win else You Loose, Word was {word}. [Note: first & last letter has to be pre-filled and there should be short description as hint for each word in json]

import csv
import random
import smtplib
from email.message import EmailMessage
import os

CSV_FILE = r"C:\\Users\\Lenovo\\OneDrive\\Desktop\\python\\participants.csv"
SENDER_EMAIL = "sendermail137@gmail.com"
SENDER_PASSWORD = "abhaya$46"


def load_participants(csv_file):
    """Load participants from CSV file"""
    participants = []
    try:
        with open(csv_file, mode="r", encoding="utf-8") as file:
            if os.stat(csv_file).st_size == 0:
                raise ValueError("CSV file is empty")

            reader = csv.DictReader(file)
            if not all(
                field in reader.fieldnames
                for field in ["Name", "Number", "Email", "Address"]
            ):
                raise ValueError(
                    "CSV file must contain columns: Name, Number, Email, Address"
                )

            for row in reader:
                if not all(row.values()):
                    continue
                participants.append(
                    {
                        "Name": row["Name"].strip(),
                        "Number": row["Number"].strip(),
                        "Email": row["Email"].strip().lower(),
                        "Address": row["Address"].strip(),
                    }
                )

        if not participants:
            raise ValueError("No valid participants found in CSV file")

        return participants

    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found at '{csv_file}'")
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")


def select_winners(participants, num_winners=3):
    """Randomly select winners ensuring no duplicates"""
    if len(participants) < num_winners:
        raise ValueError(
            f"Not enough participants (need {num_winners}, have {len(participants)})"
        )
    return random.sample(participants, num_winners)


def send_winner_email(winner, sender_email, sender_password):
    """Send congratulatory email to a winner"""
    msg = EmailMessage()
    msg["Subject"] = "Congratulations! You're a Winner!"
    msg["From"] = sender_email
    msg["To"] = winner["Email"]

    email_body = f"""
    Dear {winner['Name']},
    
    🎉 Congratulations!! 🎉
    
    You have won our lucky draw!
    
    We'll contact you soon at {winner['Number']} regarding your prize.
    
    Thank you for participating!
    
    Best regards,
    The Marketing Team
    """
    msg.set_content(email_body.strip())

    try:
        with smtplib.SMTP_SSL("subediabhaya9@gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"✓ Email sent to {winner['Name']} ({winner['Email']})")
        return True
    except Exception as e:
        print(f"✗ Failed to send email to {winner['Email']}: {str(e)}")
        return False


def main():
    print("🏆 Lucky Draw Winner Selection 🏆")
    print(f"Loading participants from: {CSV_FILE}")

    try:
        participants = load_participants(CSV_FILE)
        print(f"Loaded {len(participants)} valid participants")

        winners = select_winners(participants)

        print("\n🎉 And the winners are:")
        for i, winner in enumerate(winners, 1):
            print(f"\nWinner #{i}:")
            print(f"  Name: {winner['Name']}")
            print(f"  Phone: {winner['Number']}")
            print(f"  Email: {winner['Email']}")
            print(f"  Address: {winner['Address']}")

        print("\nSending notification emails...")
        for winner in winners:
            send_winner_email(winner, SENDER_EMAIL, SENDER_PASSWORD)

        print("\n✨ All done! Winners have been notified.")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Please check your CSV file and try again.")


if __name__ == "__main__":
    main()
