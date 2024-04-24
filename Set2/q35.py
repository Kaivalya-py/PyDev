#  Book Library System with Various Features: Create a comprehensive library management system in Python. This system should allow the user to add new book details, display all book details, search for a book using its ISBN, and exit the system. Each book record should include ISBN, title, author name, price, and genre. The system should be able to handle duplicate ISBN entries gracefully.

def add_book(books):
    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    price = float(input("Enter price: "))
    genre = input("Enter genre: ")
    books[isbn] = [title, author, price, genre]
    print("Book added successfully.")

def display_all_books(books):
    if not books:
        print("No books available.")
    else:
        print("Books:")
        for isbn in books:
            print("ISBN:", isbn)
            print("Title:", books[isbn][0])
            print("Author:", books[isbn][1])
            print("Price:", books[isbn][2])
            print("Genre:", books[isbn][3])
            print()

def search_book(books):
    isbn = input("Enter ISBN to search: ")
    if isbn in books:
        print("Book details:")
        print("ISBN:", isbn)
        print("Title:", books[isbn][0])
        print("Author:", books[isbn][1])
        print("Price:", books[isbn][2])
        print("Genre:", books[isbn][3])
    else:
        print("Book not found.")

books = {}
while True:
    print("Menu:")
    print("1. Add book")
    print("2. Display all books")
    print("3. Search book by ISBN")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 4:
        break
    elif choice == 1:
        add_book(books)
    elif choice == 2:
        display_all_books(books)
    elif choice == 3:
        search_book(books)
    else:
        print("Invalid choice")
