# This code checks the age and prints a message based on the age

age = int(input("What is your age? "))
if age >= 5:
    print(f"Ok, you're {age} years old")
elif age < 5 and age >=0:
    print(f"I suspect you can't write quite yet...")
else:
    print("That must be a mistake")
