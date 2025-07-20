string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

first_occurence = string.find(substring)
second_occurence = -1

if first_occurence != -1:
    second_occurence = string.find(substring, first_occurence + len(substring))
if second_occurence != -1:
    print(f"The second occurence of the substring is at index {second_occurence}.")
else:
    print("The substring does not occur twice in the string.")