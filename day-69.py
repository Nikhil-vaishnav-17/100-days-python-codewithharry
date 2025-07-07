#Class methods
class Employee:
    company = 'Apple'
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'The name is {self.name} and company is {self.company}')

    @classmethod
    def changeCompany(cls, company):
        cls.company = company

e1 = Employee("Harry")
e1.show()
e1.changeCompany("Tesla") #It will change the variable for whole class as class method decorator is added
e1.show()
e2 = Employee("Nikhil")
e2.show()