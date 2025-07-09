# This program asks for the hourly wage, hours worked, and the day of the week. The program then prints out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

hrly_wage = float(input("Hourly wage: "))
working_hrs = float(input("Hours worked: "))
day = str(input("Day of the week: "))

daily_wages = hrly_wage * working_hrs
if day == "Sunday":
    daily_wages *= 2
print(f"Daily wages: {daily_wages} euros")