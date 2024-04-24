# Validate IPv4 Address Format: Write a program that validates whether a given string is a valid IPv4 address, consisting of four numbers separated by dots, with each number ranging from 0 to 255.

def is_valid_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True

ip = input("Enter an IPv4 address: ")
if is_valid_ipv4(ip):
    print(ip, "is a valid IPv4 address.")
else:
    print(ip, "is not a valid IPv4 address.")
