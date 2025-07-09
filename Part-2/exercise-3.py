# This code separates the integer and fractional parts of a number input by the user.

number = float(input("Please type in a number: "))
print(f"Integer part: {int(number)}")
print(f"Fractional part: {number - int(number)}")