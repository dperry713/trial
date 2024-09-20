from math import floor  # for integer division output, optional

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    operation = input("Enter the operation (+, -, *, /): ")
    if operation in ["+", "-", "*", "/"]:
        break
    else:
        print("Invalid operation. Please enter +, -, *, or /")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue  # Go back to step 2 to get new input

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    else:
        if num2 != 0:
            result = divide(num1, num2)
        else:
            print("Error: Cannot divide by zero")
            continue

    print(f"The result is: {result}")

    # ... (after printing the result)
    another_calculation = input("Do you want to perform another calculation? (y/n): ")
    if another_calculation.lower() != "y":
        break
