#Get input string and prefix to remove.
string = input("Enter a string: ")
prefix = input("Enter prefix to be remove: ")
#Check if the string starts with the prefix
if string [ : len(prefix)] == prefix: #If yes, remove the prefix.
    string = string[len(prefix) : ]
#If no, return the string unchanged.
print ("Output: ", string)