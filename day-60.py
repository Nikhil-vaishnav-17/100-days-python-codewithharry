#Getters & Setters
class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"The value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10

Obj = MyClass(10)
print(Obj.ten_value) #I can use the getters function as a variable instead but, we cant change the value of it like: Obj.ten_value = 67
Obj.show()
Obj.ten_value = 67
Obj.show()
