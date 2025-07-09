# This program checks if a given year is a leap year or not.

year = int(input("Please type in a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"That is a leap year.")
        else:
            print(f"That year is not a leap year.")
    else:
        print(f"That is a leap year.")
else:
    print(f"That year is not a leap year.")