# This program calculates integer numbers from the user until they enter 0.
print("Please type in integer numbers. Type in 0 to finish.")

count = 0
total = 0
positive = 0
negative = 0

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    count +=1
    total += number
    if number > 0:
        positive +=1
    else:
        negative +=1
print(f'Numbers typed in {count}')
print(f"The sum of the numbers is {total}")
print(f"The mean of the number is {total / count}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")