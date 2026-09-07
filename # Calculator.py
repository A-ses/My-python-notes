# Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+": # addition
    result = num1 + num2
elif operator == "-": # subtraction
    result = num1 - num2
elif operator == "*": # multiplication
    result = num1 * num2
elif operator == "/": # division
    result = num1 / num2
else:
    print("Invalid operator")

print("Result:", result)
