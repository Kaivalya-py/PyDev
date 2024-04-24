# Swap Two Variables Without a Third Variable: Implement a program to swap the values of two variables without using a third, temporary variable. 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")


