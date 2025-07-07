#Operator overloading
#For more operators You can refer to: docs.python.org/3/reference/datamodel.html
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary > 0:
            return f"{self.real} + {self.imaginary} i"
        else:
            return f"{self.real} - {abs(self.imaginary)} i"

    def __add__(self, other):
        return Complex(self.real+other.real, self.imaginary+other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
c1 = Complex(10,20)
c2 = Complex(5,3)
print(c1)
print(c2)
print(c1+c2)
print(c1-c2)
print(c2-c1)