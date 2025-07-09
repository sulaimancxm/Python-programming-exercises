# This program asks a user for an integer number.
# If the number is below zero, the program would print out the message "invalid".
# If the number is above zero, the program print out the square root of the number.
# The program would then asks for another number. If the user inputs the number zero, the program would stop asking for numbers and exit the loop.

from math import sqrt

while True:
    number = int(input("Please type in a number: "))
    if number < 0:
        print("Invalid number")
    if number > 0:
        print(sqrt(number))
    if number == 0:
        break
print("Exiting...")

