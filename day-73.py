#Magic/ DUnder methods in class
class Employee:
    def __init__(self,name):
        self.name = name

    def __len__(self): #This can calculate the length of name by passing the object
        i = 0
        for _ in self.name:
            i+=1
        return i

    def __str__(self):
        return f'{self.name}'

    def __repr__(self): #Same as str method but it will be called if no str method is present or we use repr(obj)
        return f"Employee('{self.name}')"

    def __call__(self, *args, **kwargs): #This will make the object callable as function
        print('Hello')
e = Employee("Harry")

print(len(e)) #It will show an error if the len method is not defined in the class
print(e) #This will run fine as we have created a __str__ method in the class
print(str(e), repr(e))

e()