from math import floor  # for integer division output, optional

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

    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        else:
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2

        print(f"The result is: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    another_calculation = input("Do you want to perform another calculation? (y/n): ")
    if another_calculation.lower() != "y":
        break
