# This program asks for two integer numbers and print out which ever is greater. If the number is equal, the program should print a different message

number1= int(input("Please type in a number: "))
number2 = int(input("Plese type in another number: "))

if number1 > number2:
    print(f"The greatest number was {number1}")

elif number1 < number2:
    print(f"The greatest number was {number2}")
    
elif number1 == number2:
    print("The numbers are equal")
