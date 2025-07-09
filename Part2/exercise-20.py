# This program ask the user to type a year 

start_year = int(input("Year: "))
year = start_year + 1
while True:
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break
 
    year += 1
 
print(f"The next leap year after {start_year} is {year}")


start_year = int(input("Year: "))
year = start_year + 1
while True:
    if year % 1000 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break
    year += 1

print(f"The next leap year after {start_year} is {year}")
        