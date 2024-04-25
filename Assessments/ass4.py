class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def get_title(self):
        return self.title


class DigitalBook(Book):
    def __init__(self, book_id, title, author, file_size_mb):
        super().__init__(book_id, title, author)
        self.file_size_mb = file_size_mb


class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_titles_by_author(self, author_name):
        titles = []
        for book in self.books:
            if book.author == author_name:
                titles.append(book.get_title())
        return titles


def main():
    library = BookCollection()

    # Sample books
    book1 = Book("1", "Python Basics", "Alice Wonderland")
    library.add_book(book1)

    book2 = DigitalBook("2", "Advanced Python", "Bob Builder", "50mb")
    library.add_book(book2)

    book3 = Book("3", "Learning Python", "Alice Wonderland")
    library.add_book(book3)

    book4 = DigitalBook("4", "Python Projects", "Bob Builder", "30mb")
    library.add_book(book4)

    # Sample author name
    author_name = "Alice Wonderland"

    # Output book titles by the specified author
    print("Titles by", author_name + ":")
    titles = library.get_titles_by_author(author_name)
    for title in titles:
        print(title)


if __name__ == "__main__":
    main()
