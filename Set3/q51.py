#  Password Strength Checker Using Regex: Create a regular expression to check the strength of a password. The password should have at least 8 characters, both uppercase and lowercase letters, at least one digit, and at least one special character.

import re

def check_password_strength(password):
    return re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password)

password = input("Enter a password: ")
if check_password_strength(password):
    print("The password is strong.")
else:
    print("The password is weak.")

