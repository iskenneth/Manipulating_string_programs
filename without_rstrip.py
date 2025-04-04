#Get text
text = input("Enter your string: ")
#Start from last character
check = len(text) - 1
#While character is space, move left
while check >= 0 and text[check] == ' ':
    check -= 1
#Print characters up to that point