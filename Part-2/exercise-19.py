# This program ask a user for a PIN code until they type in the correct one.
# It then prints out the number of times the user tried different codes. 
pin = "4321"
attempts = 0
while True:
    code = input("PIN: ")
    attempts +=1
    if code == pin:
        if attempts ==1:
            print(f"Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts") 
        break
    else:
        print("Wrong")

