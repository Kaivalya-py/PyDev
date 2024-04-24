#  Menu-Driven Add/Sub/Mul/Div Operations: Develop a menu-driven program that prompts the user to choose between addition, subtraction, multiplication, or division operations on two input numbers.

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    else:
        return a / b
    
while True:
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        break
    else:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", sub(a, b))
        elif choice == 3:
            print("Result:", mul(a, b))
        elif choice == 4:
            print("Result:", div(a, b))
        else:
            print("Invalid choice")