# This program asks the user for an integer number. If the number is less than zero, the program should print out the number multiplied by -1. Otherwise the program prints out the numbers as its.

number = int(input("Please type in a number: "))
if number < 0:
    print(f"The absolute value of this number is {number * -1}")
print(f"The absolute value of this number is {number}") 