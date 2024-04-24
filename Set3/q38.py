# Display Students Scoring Above 85: Create a dictionary called 'students' where keys are student names and values are their grades. The program should display all students who scored more than 85. 

# The graes shoul be an array of integers.

def display_students_above_85(students):
    for student in students:
        if sum(students[student]) > 85:
            print(student)

students = {
    "Alice": [90, 85, 88],
    "Bob": [70, 80, 90],
    "Charlie": [85, 90, 95]
}

display_students_above_85(students)


