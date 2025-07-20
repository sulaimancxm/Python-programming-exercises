word = input("Please type in a string: ")

if len(word) > 1 and word[1] == word[-2]:
    print("The second and the second to last characters are " + word[1])
else:
    print("The second and the second to last characters are different")
 