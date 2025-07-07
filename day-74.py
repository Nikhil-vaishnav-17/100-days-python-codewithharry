#Method overriding

class Shape:
    def __init__(self,x,y):
        self.x, self.y = x, y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, x):
        super().__init__(x,x)

    def area(self): #Function is overridden in the child class
        return 3.14 * super().area()

sq = Shape(4,5)
cir = Circle(10)
print(sq.area(), cir.area())