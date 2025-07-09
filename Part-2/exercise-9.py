# This progr asks for users name.
# If the name is Huey, Dewey or Louie, the program should recognise the user is one of Donald Duck's nephews.
# if the name is Morty or Ferdie, the program should recognise the user is one of Mickey Mouse's nephews.
# if the name is not one of these, the program will print a different message

name = str(input("Please type in your name: "))
if name == "Huey" or name == "Dewey" or name == "Louie":
    print(f"I think you might be one of Mickey Mouse's nephews.")
elif name == "Morty" or name == "Ferdie":
    print(f"I think you might be one of Donald Duck's nephews.")
else:
    print(f"You're not a nephew of any character I know of.")