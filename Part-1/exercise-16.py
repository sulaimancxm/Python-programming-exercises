# This program asks the user for a number of days and then prints out the number of seconds in the amount of days given.

days = int(input("How many days? "))
seconds = days * 24 * 60 * 60
print(f"Seconds in that many days: {seconds}")
