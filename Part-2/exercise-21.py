# Fixing the code..
 
words = ""
prev_word = ""

while True:
    word = input("Please type in a word: ")

    if word == "end" or word == prev_word:
        break
    words += word + " "
    prev_word = word
    
print(words.strip())