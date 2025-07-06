# This program asks a user "Shall we continue?", if user typed "no" the loop will break. Otherwise it will keep asking "Shall we continue?".

print("hi")
while True:
    user_input = input("Shall we continue? ")
    if user_input == "no":
        break
    print("hi")
print("okay then")