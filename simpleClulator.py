#Simple Basc Python Calcuator Program 
num1 = float(input("Enter first Number:"))
num2 = float(input("Entr second Number:"))
operation = input("Enter Operation(+,-,*,/):")

#perform the operation based on user input

if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Division by zero is not allowed")
else:
    print("invalid operation .Please enter valid operation(+,-,*,/)")