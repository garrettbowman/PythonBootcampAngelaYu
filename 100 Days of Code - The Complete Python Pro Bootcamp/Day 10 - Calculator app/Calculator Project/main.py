def add(n1, n2):
    '''
    Adds two numbers together'''
    return n1 + n2

def subtract(n1, n2):
    '''
    Subtracts n2 from n1'''
    return n1 - n2

def multiply(n1, n2):
    '''
    Multiplies n1 by n2'''
    return n1 * n2

def divide(n1, n2):
    '''
    Divides n1 by n2'''
    return n1 / n2


from art import logo
print(logo)

keepcalculating = True

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

choice ="y"

while keepcalculating:
    num1= float(input("What is the first number?: "))
    if choice == "n":
        choice = "y"
    while choice == "y":
    
        operation = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        for symbol in operations:
            print(symbol)
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        elif choice == "n":
            keepcalculating = True
        else:
            keepcalculating = False