# This program asks for tomorrow's weather forecast and then suggest weather-appropriate clothing.

weather = ("What is the weather forecast for tomorrow? ")
temparature = float(input("Temparature: "))
rain = str(input("Will it rain (yes/no)"))
print("Wear jeans and a T-shirt")

if temparature <= 20:
    print("I recommend a jumper as well")
if temparature <= 10:
    print("Take a jacket with you")
if temparature <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")