# Day 2 - Python Basics: Simple Calculator Program
# Covers: Variables, Data Types, Operators, Loops, Functions

# Function to perform calculation based on operator
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    else:
        return "Invalid operator!"

# Main program using a loop so user can calculate multiple times
while True:
    # Variables storing user input (converted to float - a data type)
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    # Calling the function and storing result in a variable
    result = calculate(num1, num2, operator)

    # Printing the result
    print(f"Result: {result}")

    # Displaying data types (to show understanding of data types)
    print(f"Type of num1: {type(num1)}, Type of num2: {type(num2)}")

    # Asking if user wants to continue (loop control)
    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != 'yes':
        print("Thank you for using the calculator!")
        break
