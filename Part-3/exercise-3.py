# This program prints out every third number, but only as long as the number is less than 100 and not divisible by 5:

number = int(input("Please type in a number: "))

while number < 100 and number % 5 != 0:
    print(number)
    number += 3
    
