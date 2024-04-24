# Store and Display Top-Scoring Student Details: Design a Python program to store details of students including their registration number, name, and marks in three subjects. The program should be able to identify and display the details of the student or students who have achieved the highest total mark.

def store_student_details():
    students = []
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        reg_no = input("Enter registration number of student " + str(i+1) + ": ")
        name = input("Enter name of student " + str(i+1) + ": ")
        marks = []
        for j in range(3):
            marks.append(int(input("Enter marks in subject " + str(j+1) + ": ")))
        students.append([reg_no, name, marks])
    return students

def display_top_scorers(students):
    highest_total = 0
    for student in students:
        total = sum(student[2])
        if total > highest_total:
            highest_total = total
    print("Top scorers:")
    for student in students:
        total = sum(student[2])
        if total == highest_total:
            print("Registration number:", student[0])
            print("Name:", student[1])
            print("Total marks:", total)
            print()

students = store_student_details()
display_top_scorers(students)