#Input: Get a string from the user.
string = input("Enter a string: ")
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
#Loop: Go through each character in the string.
swapcase = ""

for char in string:
    if char in uppercase:
    swapcase += lowercase[uppercase.index(char)]
    elif char in lowercase:
        swapcase += uppercase[lowercase.index(char)] 
    else:
        swapcaee += char

#Output: Print the modified string.