class Employee:
    pass
class Dancer:
    pass

class DancerEmployee(Dancer, Employee):
    def __init__(self, name:str, dance:str):
        self.name = name
        self.dance = dance