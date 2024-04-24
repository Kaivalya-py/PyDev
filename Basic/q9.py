# Check if a Number is Positive, Negative, or 0: Write a program that determines whether a user-inputted number is positive, negative, or zero. 

n = float(input("Enter a number: "))
if n > 0:
    print("The number is positive.")
elif n < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
