# Extract URLs from a String: Develop a Python script to extract all URLs from a given string, assuming URLs start with http:// or https:// and end with a space or punctuation.

import re

def extract_urls(text):
    return re.findall(r"https?://\S+", text)

text_with_urls = """
Here are some URLs: http://www.example.com, https://www.google.com,
http://www.website.net, https://www.python.org
"""

urls = extract_urls(text_with_urls)

for url in urls:
    print(url)
