from logo import logo

print(logo)


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
    "/": divide
}

should_end = False

first_number = int(input("What is your first number?: "))

while not should_end:

    for symbol in operations:
        print(symbol)

    operator = input("Pick an operator: ")

    second_number = int(input("What's your next number?: "))

    calculation_function = operations[operator]
    result = calculation_function(first_number, second_number)

    print(f"{first_number} {operator} {second_number} = {result}")

    restart = input(
        f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or 's' to stop ")

    if restart == 's':
        should_end = True
        print('Thanks for playing.')
    elif restart == 'n':
        first_number = int(input("What is your first number?: "))
    else:
        first_number = result
