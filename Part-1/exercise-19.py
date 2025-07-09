# This program asks the user for four numbers and then prints out teh sum and the mean of the numbers.

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))
Number4 = int(input("Number 4: "))

total_sum = number1 + number2 + number3 + Number4
mean = total_sum / 4

print(f"The sum of the numbers is {total_sum} and the mean is {mean}")