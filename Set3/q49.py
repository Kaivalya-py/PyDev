# Validate Date Format Using Regex: Implement a program that uses regular expressions to verify if a given date string is in the format DD/MM/YYYY.

import re

def validate_date(date):
    return re.match(r"\d{2}/\d{2}/\d{4}", date)

date = input("Enter a date (DD/MM/YYYY): ")
if validate_date(date):
    print("The date format is valid.")
else:
    print("The date format is invalid.")
