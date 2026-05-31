print("Simple Calculator")

while True:

    a = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if operation == "+":
        result = a + b

    elif operation == "-":
        result = a - b

    elif operation == "*":
        result = a * b

    elif operation == "/":
            
        if b == 0:
            result = "Error: Division by zero"   

        else:
            result = a / b

    else:
        result = "Unknown operation"

    print("Result:", result)