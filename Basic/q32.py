# List Fibonacci Numbers in a Range: Develop a program to generate and display the Fibonacci numbers within a specified range. 

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def list_fibonacci(start, end):
    n = 0
    while fibonacci(n) <= end:
        if fibonacci(n) >= start:
            print(fibonacci(n), end=' ')
        n += 1

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print("Fibonacci numbers between", start, "and", end, "are:")
list_fibonacci(start, end)
