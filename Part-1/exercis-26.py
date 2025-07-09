# This program asks the user for two numbers and an operation. If the operation is add, multiply, or subtract, the program then calculate and print out the result of the operation with the given numbers.
# If the user types in anythig else the program prints nothing!

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    
    print(f"{num1} + {num2} = {num1 + num2}")

if operation == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")

if operation == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")