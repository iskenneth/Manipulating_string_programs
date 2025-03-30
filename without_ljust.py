#Get input string and desired length.
string = input ("Enter your string: ")
justify = int(input("Enter desired justify length: "))
#Calculate how many spaces are needed to reach the length.
if len(string) < justify:
    string += " " * (justify - len(string)) #Append the required spaces at the end of the string.
#Print the modified string.
print (string)