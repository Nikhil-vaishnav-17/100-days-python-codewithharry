#Access Modifiers

"""In python There is no access modifiers like public, private or protected"""

class Employee:
    def __init__(self):
        self.name = "Harry"
        self.__age = 20
        self._surname = 'Bhai'

a = Employee()
print(a.name) #It can be access directly
# print(a.__age) It will show an error as it cannot be accessed directly

# noinspection PyUnresolvedReferences,PyProtectedMember
print(a._Employee__age) #You can access like this if you put a double '_' in the name

#For a protected variable or function you can use a single '_' before the name.
print(a._surname) #It will not show an error while running the code but it is used to show that it is protected and should not be accessed