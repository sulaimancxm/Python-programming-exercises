# This program asks the user for an integer number.
# If the number is divisible by 3, the program will print Fizz.
# If the number is divisible by five, the programm will print Buzz.
# If the number is divisible by both three and five, the program will print out Buzz

number = int(input("Number 1: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)