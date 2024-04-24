# Scholarship Eligibility for First Graduates: Write a program to determine if a student, who is the first graduate in their family and has scored an average of over 98 in math, physics, and chemistry, is eligible for a scholarship.

sub1 = float(input("Enter marks in Math: "))
sub2 = float(input("Enter marks in Physics: "))
sub3 = float(input("Enter marks in Chemistry: "))
average = (sub1 + sub2 + sub3) / 3
if average > 98:
    print("Congratulations! You are eligible for a scholarship.")
else:
    print("Sorry! You are not eligible for a scholarship.")
    