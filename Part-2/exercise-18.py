# This program asks the user for a password.
# It will then asks the user to repeat the password.
# If the user types in something else than the first password, the program should keep on asking untill the user types the first password again correctly

passwd = input("Password: ")
while True:

    repeat_passwd = input("Repeat password: ")
    if passwd == repeat_passwd:
        break
    print("They do not match!") 
print("User account created!")