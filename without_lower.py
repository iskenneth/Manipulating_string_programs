# Get input string
string = input("Enter a string: ")
# Initialize empty string to store lowercase result
lowercase = ""
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
# Loop through each character in the string
for char in string:
    # Check if the character is an uppercase letter ('A' to 'Z')
    if char  in uppercase:
        # Find the index of the uppercase letter in uppercase string
        index = uppercase.index(char)
        # Get the corresponding lowercase letter
        lowercase += lowercase_letters[index]
    else:
        lowercase += char  
# Print the result
print ("Output: ", lowercase)