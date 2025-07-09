# This program calculates the amount of gift tax to be paid in Finland based on the value of a gift received from a close relative

gift_value = int(input("Value of gift: "))

if gift_value < 5000:
    print("No tax!")
elif gift_value < 25000:
    tax = 100 + (gift_value - 5000) * 0.08
    print(f"Amount of tax: {tax} euros")
elif gift_value < 55000:
    tax = 1700 + (gift_value - 25000) * 0.10
    print(f"Amount of tax: {tax} euros")
elif gift_value < 200000:
    tax = 4700 + (gift_value - 55000) * 0.12
    print(f"Amount of tax: {tax} euros")
elif gift_value < 1000000:
    tax = 22100 + (gift_value - 200000) * 0.15
    print(f"Amount of tax: {tax} euros")
else:
    tax = 142100 + (gift_value - 1000000) * 0.17
    print(f"Amount of tax: {tax} euros")