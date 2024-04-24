#  Check if a String is a Palindrome: Write a program to determine if a given string is a palindrome. 

def is_palindrome(s):
    if len(s) < 2:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

s = input("Enter a string: ")
if is_palindrome(s):
    print(s, "is a palindrome.")
else:
    print(s, "is not a palindrome.")
