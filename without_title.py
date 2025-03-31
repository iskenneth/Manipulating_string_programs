#Get the input string.
string = input("Enter a string: ")
#Split the string into words.
words = string.split()
#Convert the first letter of each word to uppercase and the rest to lowercase.
for word in words:
    title = word[ 0 ].upper() + word[ 1: ].lower()

#Join the words back together and print the result.