#Map, filter and reduce function usage

num = [1,2,3,4,5,6]
print(num)
#Map function
square = lambda x : x*x
num2 = map(square,num) #Map iterate throwout the list and use the function on every single element. 'map(function,iterable)'
print(list(num2))
#we can use lambda function to do the same: map(lambda x : x*x, num)

#Filter function
func = lambda x: x>3
num2 = filter(func,num) #filter iterate through the list use the function on every single variable but,
                        #it only accepts True or False statements, if the function returns true it will stay in the list otherwise Not.
print(list(num2))

#reduce function
from functools import reduce
num2 = reduce(lambda x,y : x+y, num) #It will reduce all the list items with the function,
                                     #like if we want to add all the list numbers we can use reduce function to do the job
print(num2)