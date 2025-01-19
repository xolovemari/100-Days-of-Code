import re
from art import logo

print(logo)

def is_valid_number(input_string):
    return bool(re.match(r'^-?\d+(\.\d+)?$', input_string))

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_accumulate = True

    number1 = input("What's the first number?: ")
    if not is_valid_number(number1):
        print("Invalid number, please try again.")
        return
    number1 = float(number1)

    while should_accumulate:
        operator = input("+\n-\n*\n/\nPick an operation: ")
        if operator not in operations:
            print("Invalid operator, please try again.")
            return

        number2 = input("What's the next number?: ")
        if not is_valid_number(number2):
            print("Invalid number, please try again.")
            return
        number2 = float(number2)

        if operator == '/' and number2 == 0:
            print("Cannot divide by zero. Please try again.")
            continue

        answer = operations[operator](number1, number2)
        
        print(f"{number1} {operator} {number2} = {answer}\n")

        new_calculation = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
        if new_calculation == 'y':
            number1 = answer
        elif new_calculation == 'n':
            should_accumulate = False
            print("\n" * 20)
            calculator()
        else:
            print("Invalid input, please try again.\n")
            calculator()

calculator()