def calculator():
    print("Make math easy with this Simple Calculator!")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        
        if operation == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()
