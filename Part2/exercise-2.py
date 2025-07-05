# This code counts the number of letters in a word input by the user.

word = str(input("Please type in a word: "))
length = len(word)
if length > 1:
    print(f"There are letters {length} in the word {word}")
print("Thank you!")