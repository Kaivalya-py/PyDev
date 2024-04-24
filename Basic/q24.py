#  Calculate Factorial of a Number: Write a program to calculate the factorial of a given number 'n'. 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number: "))
print("Factorial of", n, "is", factorial(n))
