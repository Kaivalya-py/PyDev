# Find Sum of Digits: Create a program to find and display the sum of the digits of a given number. 

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
    
n = int(input("Enter a number: "))
print("Sum of digits of", n, "is", sum_of_digits(n))