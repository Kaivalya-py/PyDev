# Algorithm for Average Marks and Pass/Fail Check: Write an algorithm that calculates a student's average marks and checks whether they have passed or failed, based on a minimum average mark of 65.

sub1 = float(input("Enter marks in the first subject: "))
sub2 = float(input("Enter marks in the second subject: "))
sub3 = float(input("Enter marks in the third subject: "))
average = (sub1 + sub2 + sub3) / 3
print(f"The average marks in the three subjects is {average}.")
if average >= 65:
    print("Congratulations! You have passed.")
else:
    print("Sorry! You have failed.")
