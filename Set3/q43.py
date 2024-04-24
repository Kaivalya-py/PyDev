#  Sort Dictionary by Values: Write a Python program to sort a dictionary by its values. For example, given a dictionary with student names as keys and marks as values, sort and display the dictionary based on marks.

def sort_dict_by_values(d):
    for key, value in sorted(d.items(), key=lambda item: item[1]):
        print(key, value)
    
students = {
    "Alice": 90,
    "Bob": 80,
    "Charlie": 85
}

sort_dict_by_values(students)
