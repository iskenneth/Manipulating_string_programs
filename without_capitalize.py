#Get the input string.
string = input("Enter a string: ")
#If the string is not empty:
if string:
    capitalized = string[0].upper() + string [ 1: ].lower()
else:
    capitalized = ""
#Print the modified string.
print("Output: ", capitalized)