# Calculate Library Book Return Fine: Develop a program to calculate the fine for returning a library book past the due date, based on the criteria provided.

days = int(input("Enter the number of days the book is late: "))
fine = 0

if days <= 0:
    print("Invalid input.")
elif days <= 7:
    fine = days * 0.10
    print(f"The fine is ${fine}.")
elif days <= 14:
    fine = 7 * 0.10 + (days - 7) * 0.20
    print(f"The fine is ${fine}.")
else:
    fine = 7 * 0.10 + 7 * 0.20 + (days - 14) * 0.30
    print(f"The fine is ${fine}.")
