from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def sub(n1, n2):
    return n1 - n2

#Multiply
def mult(n1, n2):
    return n1 * n2

#Divide
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def calculator():
    print(logo)
    flag = True
    
    num1 = float(input("What's the first number?: "))

    for operation in operations:
        print(operation)

    while flag:
        operationSymbol = input("Pick an operation: ")
        calculationFunction = operations[operationSymbol]
        
        num2 = float(input("What's the next number?: "))
        
        answer = calculationFunction(num1, num2)
        
        print(f"{num1} {operationSymbol} {num2} =  {answer}")
        
        if input(f"Type Y to continue calculation with {answer} or N to start new calculation") == "y":
            num1 = answer
        else:
            flag = False
            calculator()

calculator()