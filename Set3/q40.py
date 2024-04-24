# Display Fruits with Indices: Create a tuple named 'fruits' containing several fruit names. Write a program that displays each fruit's name along with its index in the tuple.

def display_fruits_with_indices(fruits):
    for index, fruit in enumerate(fruits):
        print(index, fruit)

fruits = ("Apple", "Banana", "Cherry", "Date", "Elderberry")
display_fruits_with_indices(fruits)

