#'is' or '==' difference

#is keyword compare the location of the memory
#== operator compares the value of the memory

a = [4]
b = [4]
print(a is b) #It will return true if a&b were not a list because python will point to same memory location if the variable is same
print(a == b)