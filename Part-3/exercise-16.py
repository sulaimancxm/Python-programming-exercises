word = input("Word: ")
frame_width = 30

border = "*" * frame_width
centred_line = f"*{word:^{frame_width-2}}*"


print(border)
print(centred_line)
print(border)