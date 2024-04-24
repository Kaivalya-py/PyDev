# Program to Check Divisibility by a Given Number: Write a program that checks if a user-inputted number is divisible by another specified number.

n = int(input("Enter a number: "))
divisor = int(input("Enter a divisor: "))
if n % divisor == 0:
    print(f"{n} is divisible by {divisor}.")
else:
    print(f"{n} is not divisible by {divisor}.")

