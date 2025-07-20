string = input("Please type in a string: ")
char = input("Please type in a single character: ")

index = string.find(char)
if index != -1 and index <= len(string) - 3:
    print(string[index:index+3])