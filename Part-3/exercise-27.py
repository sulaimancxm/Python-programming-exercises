number = int(input("Please type in a number: "))
start = 1
end = number
while start <= end:
    print(start)
    if start != end:
        print(end)
    start += 1
    end -= 1