#Get input string and suffix to check.
string = input ("Enter a string: ")
ending = input ("Enter suffix to detect: ")
#Compare the last characters of the string with the suffix
if len(ending) <= len(string) and string[- len(ending) : ] == ending:
#If they match, print True, else print False.