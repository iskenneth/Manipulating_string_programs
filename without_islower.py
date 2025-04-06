#Ask user for text
Input = input("Enter a string: ")
#Assume all letters are lowercase
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
islower = True 

#For each letter: If it's an uppercase letter, set result to false
for letter in Input:
    if letter in upper:
        islower = False
        break
#Show result
print(islower)