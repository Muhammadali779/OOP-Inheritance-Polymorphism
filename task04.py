import math

class Shape:
   def __init__(self):
       pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Triangle(Shape):
    def __init__(self, c, h):
        self.c = c
        self.h = h

    def area(self):
        return 0.5 * self.c * self.h

shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 8)
]

for s in shapes:
    print(f"S = {s.area():.2f}")
