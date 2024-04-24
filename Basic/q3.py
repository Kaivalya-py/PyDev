# Find Largest and Smallest Among 3 Numbers: Create a program to compare three numbers input by the user and determine the largest and smallest among them. 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print(f"{a} is the largest number.")
elif b > a and b > c:
    print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number.")

if a < b and a < c:
    print(f"{a} is the smallest number.")
elif b < a and b < c:
    print(f"{b} is the smallest number.")
else:
    print(f"{c} is the smallest number.")
