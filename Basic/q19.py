# Convert Integer to Binary, Octal, and Hex: Develop a program that converts a given integer to its binary, octal, and hexadecimal equivalents.

n = int(input("Enter an integer: "))
binary = bin(n)
octal = oct(n)
hexadecimal = hex(n)

print(f"The binary equivalent of {n} is {binary}.")
print(f"The octal equivalent of {n} is {octal}.")
print(f"The hexadecimal equivalent of {n} is {hexadecimal}.")
