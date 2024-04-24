# Record and Display Student Pairs for Projects: Write a Python program to manage student pairs for class projects. The program should allow pairing two students, displaying all pairs, and exiting the program. It should maintain a list of student pairs, where each pair is a tuple containing the names of the two students.

def pair_students():
    student_pairs = []
    while True:
        print("Menu:")
        print("1. Pair students")
        print("2. Display all pairs")
        print("3. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            student1 = input("Enter name of student 1: ")
            student2 = input("Enter name of student 2: ")
            student_pairs.append((student1, student2))
            print("Students paired successfully.")
        elif choice == 2:
            if not student_pairs:
                print("No pairs available.")
            else:
                print("Student pairs:")
                for pair in student_pairs:
                    print(pair[0], "and", pair[1])
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

pair_students()