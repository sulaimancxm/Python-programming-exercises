# This program finds the next leap year after a given year that the user inputs. 

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