#Get input string.
string = input("Enter a string with a leading spaces: ")
#Loop through characters from the beginning:
i = 0
while i <  len(string) and string[i] == " ":
    i += 1
#Print the remaining string.
print ("Output: ", string[i:])