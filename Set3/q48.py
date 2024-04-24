#  Extract Email Addresses Using Regex: Write a Python script that uses regular expressions to extract all email addresses from a given text.

import re

def extract_emails(text):
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

text_with_emails = """
Here are some email addresses: john.doe@example.com, mary.smith123@gmail.com,
info@company.net, support@website.co.uk
"""

emails = extract_emails(text_with_emails)

for email in emails:
    print(email)