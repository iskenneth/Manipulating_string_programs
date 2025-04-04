#Ask the user to enter text  
text = input("Enter your string: ")
#define the value of lower and capital letter
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
#create a result storage
output = ""
#For each letter in the text:  ,If the letter is in small letters:    Find its position in small letters    Add the letter from big letters at the same position to result 
for letter in text:
    if letter in text in lower:
        index = lower.index(letter) 
        output += capital(index)
else:
    output += letter
#Show the result
