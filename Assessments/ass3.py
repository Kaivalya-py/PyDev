import re

def validate_url(url):
    pattern = r'^https?://(?:\w|-)+(?:\.(?:\w|-)+)+(?:/[^/]+)*$'
    if re.match(pattern, url):
        return True
    else:
        return False

# Example usage:
print(validate_url("https://example1.com"))  
print(validate_url("http://subdomain.example2.com/path/to/page"))  
print(validate_url("https://example3.com?query=1&param=2"))  
print(validate_url("https://sub.domain.example4.com"))  
print(validate_url("https://example5.com/path/to/page.html"))  

# Output:
