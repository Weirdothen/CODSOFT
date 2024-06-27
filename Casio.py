def add(a, b):
    # Function to add two numbers
    return a + b

def subtract(a, b):
    # Function to subtract second number from first number
    return a - b

def multiply(a, b):
    # Function to multiply two numbers
    return a * b

def divide(a, b):
    # Function to divide first number by second number
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

print("Welcome to the simple calculator!")

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user
operation_choice = input("Enter choice (1/2/3/4): ")

if operation_choice in ['1', '2', '3', '4']:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if operation_choice == '1':
        print(f"The result is: {add(number1, number2)}")

    elif operation_choice == '2':
        print(f"The result is: {subtract(number1, number2)}")

    elif operation_choice == '3':
        print(f"The result is: {multiply(number1, number2)}")

    elif operation_choice == '4':
        print(f"The result is: {divide(number1, number2)}")
else:
    print("Invalid input. Please select a valid operation.")
