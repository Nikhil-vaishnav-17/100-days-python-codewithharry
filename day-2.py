a = 13
b = "Harry"
print(a,b, type(b))
b = 11
print(a+b, type(b))

a = complex(5,5) #complex
b = True #bool
c = 11.1 #float
d = None #None data type

print(type(a), type(b), type(c), type(d))

list1 = [1,8.11, "Nikhil", [1,8]] #list data type
print(list1, type(list1))

tuple1 = (("parrot", "sparrow"),("Hello", "World")) #tuple, cannot be modified after creation
print(tuple1, type(tuple1))

dist1 = {'Name':"Nikhil", 'age' : 20, 'can vote': True} #dictionary
print(dist1, type(dist1))