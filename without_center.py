#Get input string and desired length.
string = input("Enter a string: ")
margin = int(input("Enter desire margin: "))
#Calculate spaces needed on both sides.
if len(string) < margin:
    total_spaces = margin - len(string)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    string = ' ' * left_spaces + string + ' ' * right_spaces
#Print the modified string.
print(string)