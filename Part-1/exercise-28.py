# This program calculates the end of a year bonus a customer receives on their loyalty card.

points = float(input("How many points are on your card? "))

if points < 100:
    # Apply 10% bonus
    new_points = points * 1.10
    print("Your bonus is 10%")
else:
    # Apply 15% bonus
    new_points = points * 1.15
    print("Your bonus is 15%")

print(f"You now have {new_points} points")