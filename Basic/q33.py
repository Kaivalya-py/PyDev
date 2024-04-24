# Check if a Number is a Fibonacci Number: Write a program to determine if a given number is part of the Fibonacci sequence.

def is_fibonacci(n, a=0, b=1):
    if n == 0:
        return True
    if a > n:
        return False
    if a == n:
        return True
    return is_fibonacci(n, b, a + b)

n = int(input("Enter a number: "))
if is_fibonacci(n):
    print(n, "is a Fibonacci number.")
else:
    print(n, "is not a Fibonacci number.")
