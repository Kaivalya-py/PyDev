# Implement a Python class named `Rectangle` that is initialized with `length` and `width`. Include the following methods: `calculate_area()` that returns the area of the rectangle. `calculate_perimeter()` that returns the perimeter of the rectangle. Additionally, create a method `display()` that prints the length, width, area, and perimeter of the rectangle. 

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.calculate_area()}")
        print(f"Perimeter: {self.calculate_perimeter()}")
        print()

r = Rectangle(5, 10)
r.display()
r = Rectangle(3, 7)
r.display()
r = Rectangle(8, 12)
r.display()