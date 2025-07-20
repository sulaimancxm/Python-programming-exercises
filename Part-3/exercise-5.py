# This program prints out the power of two in order.

limit = int(input("Upper limit: "))  # This line asks the user to type in an upper limit number.

number = 1  # Initialize the first number to print

while number <= limit: # Loop while the current number is less than or equal to the limit
    print(number) # Print the current number
    number *=2  # Double the number for the next iteration
    