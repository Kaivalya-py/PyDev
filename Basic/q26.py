#  Check if a Number is a Palindrome: Implement a program to check whether an input number is a palindrome.

def is_palindrome(n):
    if n < 10:
        return True
    else:
        return str(n) == str(n)[::-1]

n = int(input("Enter a number: "))
if is_palindrome(n):
    print(n, "is a palindrome.")
else:
    print(n, "is not a palindrome.")