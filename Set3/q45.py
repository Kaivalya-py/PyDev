# Sort People by Height in Descending Order: Given a list of tuples, each containing a person's name and height, write a program to sort this list by height in descending order.

def sort_people_by_height(people):
    for name, height in sorted(people, key=lambda x: x[1], reverse=True):
        print(name, height)

people = [
    ("Alice", 5.5),
    ("Bob", 6.0),
    ("Charlie", 5.8)
]

sort_people_by_height(people)