number = int(input("Please type in a number: "))
while number > 0:
    i = 1
    while i < number:
        print(f"{i} ", end="")
        i += 1
    print()
    number -= 1
    