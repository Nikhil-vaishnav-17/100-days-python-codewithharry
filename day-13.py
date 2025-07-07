#Strings are immutable so all the functions will not change the string, it just prints the new string created by the functions
a = 'nIkHiL vaIsHnAv'
print(a.upper()) #All uppercase
print(a.lower()) #All lowercase

test = '!!!! ahkdsgha !!!!!!!!!!!!'
print(test.rstrip("!")) #remove leading '!' not in start
print(a.replace("n", "M")) #replace all N to M ( case sensitive)
print(a.split(" ")) #splits when finds a ' '
print(a.capitalize()) #capitalize first character and lowercase all others
print(a.center(20)) #Give starting ' ' when used. Like the length of a is 15 so it will have 5 starting ' '
print(a.count("n")) #count all n in the string (case-sensitive)
print(a.endswith("v")) #Boolean return type will check if the string ends with v or not

str1 = "Welcome to the console!!!"
print(str1.endswith("to",4,10)) #slice the string from 4-10 before checking the endswith string
print(str1.find("to")) #find the index of the character or string

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # returns true if it consists of alphanumeric value
print(str1.isalpha()) #check if it is only alphabets or not
'''
islower() : checks if all the characters are lowercase
isprintable(): checks if the string is printable characters or not, non printable characters ex: \n, \t etc
isspace(): if all the string contains whitespace
istitle() : check if the first character of all the words are uppercase
startswith() : check if the string starts with the given string or character
swapcase() : change all uppercase to lowercase and vice versa
title() : change the string to a title, means it will convert all the first characters of the word to uppercase
'''