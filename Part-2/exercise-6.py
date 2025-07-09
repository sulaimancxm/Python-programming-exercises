# This program compares the ages of two people and determines who is older

print("Person 1: ")
name1 = str(input("Name 1:"))
age1 = int(input("Age: "))

print("Person 2: ")
name2 = str(input("Name 2:"))
age2 = int(input("Age 2: "))

if age1 > age2:
    print(f"The elder is {name1}.")
elif age1 < age2:
    print(f"The elder is {name2}.")
else:
    print(f"{name1} and {name2} are the same age.")