#  Populate Dictionary with Book Characters: Given a list of tuples containing character names and the books they appear in, create a dictionary where keys are unique book titles and values are sets containing the names of characters in each book. 

def populate_dict_with_book_characters(characters):
    books = {}
    for character, book in characters:
        if book not in books:
            books[book] = set()
        books[book].add(character)
    print(books)

characters = [
    ("Alice", "Book1"),
    ("Bob", "Book2"),
    ("Charlie", "Book1"),
    ("Alice", "Book2")
]

populate_dict_with_book_characters(characters)

