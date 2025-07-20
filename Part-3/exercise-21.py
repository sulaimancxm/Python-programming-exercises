word = input("Please type in a word: ")
char = input("Please type in a word: ")

while len(word) >= 3:

    if word[0] == char:
        print(word[:3])
    word = word[1:]