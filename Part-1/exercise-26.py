# This program asks the user for a temparature in degrees Fahrenheit, and then prints out the same in degrees Celsius, If the converted temparature falls below zero degrees Celsius, the program also prints out "Brr! It's cold in her!" .

fahrenheit = int(input("Please type in a temparature (F): "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print("Brr! It's cold in here!")