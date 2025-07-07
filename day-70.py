#Class methods as alternative constructors

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f'The name is {self.name} and has {self.salary}')

    @classmethod
    def fromStr(cls, string):
        return cls(string.split('-')[0], int(string.split('-')[1])) #Returns an class object

e1 = Employee('Nikhil', 12000)
e1.show()
emp_string= 'Harry-10000'
# e2 = Employee(string.split('-')[0], string.split('-')[1])
# e2.show()
#Instead of doing this we can create a class method as constructor
e2 = Employee.fromStr(emp_string) #This will create a new object
e2.show()