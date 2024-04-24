# Display Odd Multiples of an Odd Number: Create a program that displays all odd multiples of an odd number within a specified range.

def display_odd_multiples(start, end, odd_num): 
    if odd_num <= 0 or odd_num % 2 == 0: 
        print("Invalid odd number. Please enter a positive odd number.") 
        return 
    for num in range(start, end + 1): 
        if num % 2 != 0 and num % odd_num == 0: 
            print(num, end= ' ') 
 
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
odd_num = int(input("Enter an odd number: "))
display_odd_multiples(start, end, odd_num)
