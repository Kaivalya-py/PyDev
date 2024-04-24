# Display Pre-2000 Published Books: Create a tuple of dictionaries, each containing details of a book. Write a program to display all books published before the year 2000.

def display_pre_2000_books(books):
    for book in books:
        if book["year"] < 2000:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])
            print()

books = [
    {"title": "Book1", "author": "Author1", "year": 1999},
    {"title": "Book2", "author": "Author2", "year": 2001},
    {"title": "Book3", "author": "Author3", "year": 1997}
]
display_pre_2000_books(books)