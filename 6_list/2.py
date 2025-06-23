# You are running small library. Store books in list book_list . Take name of book student want from input. If book exists in list, remove it from list & print final list by sorting but if it doesn’t exist print Book, {book_name} not found.
book_list = [
    "Harry Potter",
    "The Hobbit",
    "To Kill a Mockingbird",
    "1984",
    "atomic habit",
]
book_name = input("Enter the name of the book you want: ")
if book_name in book_list:
    book_list.remove(book_name)
    book_list.sort()
    print("Updated book list :", book_list)
else:
    print(f"Book, {book_name} not found.")
