# Get input string
string = input("Enter a string: ")
# Initialize empty string to store lowercase result
lowercase = ""
# Loop through each character in the string
for char in string:
    # Check if the character is an uppercase letter ('A' to 'Z')
    if 'A'  <= char <= 'Z' :
        # Convert to lowercase by using ASCII character mapping
        lowercase += chr(char + ('a' - 'A'))
    else:
        lowercase += char 
    
# Print the result