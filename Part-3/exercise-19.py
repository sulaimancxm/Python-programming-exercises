input_string = "perpendicular"

while True:
    substring = input("Please type in a string: ")
    index = input_string.find(substring)
    if index >= 0:
        print(f"Found it at the index {index}")
    else:
        print("Not found")
