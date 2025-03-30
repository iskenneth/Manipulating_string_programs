#Get input string.
string = input("Enter a string with a leading spaces: ")
#Loop through characters from the beginning:
i = 0
while i < 0 len(string) and string[i] == " ":
    i += 1
#If the character is a space, move to the next character.
#If the character is not a space, stop looping.
#Print the remaining string.