# Print Numbers Divisible by 'n': Implement a program that prints all numbers within a certain range that are divisible by a given number 'n'.

n = int(input("Enter a number: "))
divisor = int(input("Enter a divisor: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Numbers divisible by {divisor} in the range {start} to {end}:")
for i in range(start, end + 1):
    if i % divisor == 0:
        print(i, end=" ")
