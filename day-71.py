#dir, _dict_ & help
from tkinter.font import names

x = [1,2,3]
print(dir(x)) #Dir can show all the methods and attributes present in the class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
print(p.__dict__) #Shows all the attributes as dictionary

help(Person)