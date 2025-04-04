#Ask for text
string = input("Enter a string: ")
#Ask for suffix
suffix = input("What is your suffix?")
#If text ends with suffix, remove it
if string[-len(suffix) : ] == suffix:
    print(string[: -len(suffix)]) 
else: 
    print(string)
#Print result