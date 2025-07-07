#string slicing
fruit = 'Mango'
print(len(fruit)) #Length of string : 5
print(fruit) # prints full string : Mango
print(fruit[1]) #prints one character : a
print(fruit[0:4]) #prints 0-4 but 4 not included so : Mang
print(fruit[1:4]) #prints 1-4 but 4 not included so : ang
print(fruit[3:]) #prints 3-end of string : go
print(fruit[:3]) #prints start-3 but 3 is not included of string : Man
print(fruit[1:-1]) #prints 1-last 1 character : ang
print(fruit[-4:-1]) # prints last 4th character to last 1 character : ang


#using loops
for i in fruit:
    print(i)