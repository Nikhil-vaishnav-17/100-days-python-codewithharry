#Walrus operator

# a = True
# print(a:=False) #This will reset it to false
#
# numbers = [1,2,3,4,5]
#
# while (n:= len(numbers)) > 0:
#     print(numbers.pop())

foods = list()
while True:
    food = input("Enter the food you like: ")
    if food == 'quit':
        break
    foods.append(food)
print(foods)
#This work can be done with same as:

foods = list()
while (food := input("Enter the food you like: ")) != 'quit':
    foods.append(food)
print(foods)