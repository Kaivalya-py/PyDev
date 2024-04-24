# Complex Number Operations: Create a program that allows the user to perform addition, subtraction, or multiplication on two complex numbers.

import math

real1 = float(input("Enter the real part of the first complex number: "))
imag1 = float(input("Enter the imaginary part of the first complex number: "))
real2 = float(input("Enter the real part of the second complex number: "))
imag2 = float(input("Enter the imaginary part of the second complex number: "))
complex1 = complex(real1, imag1)
complex2 = complex(real2, imag2)

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
choice = int(input("Enter your choice: "))
if choice == 1:
    result = complex1 + complex2
    print(f"The sum of the two complex numbers is {result}.")
elif choice == 2:
    result = complex1 - complex2
    print(f"The difference of the two complex numbers is {result}.")
elif choice == 3:
    result = complex1 * complex2
    print(f"The product of the two complex numbers is {result}.")
else:
    print("Invalid choice.")