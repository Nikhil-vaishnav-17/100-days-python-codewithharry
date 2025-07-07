#Inheritance overview

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print(f"The default language for {self.id} is python")

e1 = Programmer("Neeraj", 100)
e1.showDetails()
e1.showLanguage()

e2 = list()

e2.append(Programmer("Harsh", 200))
e2[0].showDetails()

print(type(e2), type(e2[0]))