#Super keyword

class ParentClass:
    def parent_method(self):
        print("This is parent method")

class Child(ParentClass):
    def parent_method(self):
        print("This is called by child class")
    def child_Method(self):
        print("This is child_method")
        super().parent_method() #This will call the method from parent class

child_object = Child()
child_object.child_Method()
child_object.parent_method() #It will call the child method if it is overridden in the class if it is not then it will call the parent class

class Employee:
    def __init__(self, name, id_):
        self.name = name
        self.id_ = id_

class Programmer(Employee):
    def __init__(self, name, id_, lang):
        super().__init__(name,id_) #It will call the constructor of parent class
        self.lang = lang

    def show(self):
        print(f'{self.name} has {self.id_} and uses {self.lang}')

p = Programmer('Nikhil', 123, 'Py')
p.show()