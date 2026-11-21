import math as m
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else 'Not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radios):
        super().__init__(color, is_filled)
        self.radios = radios

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {m.pi * pow(self.radios, 2)}cm^2\n")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        super().describe()
        print(f"It is a square with an area of {pow(self.width, 2)}cm^2\n")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        super().describe()
        print(f"It is a triangle with an hypotenuse of {m.sqrt(pow(self.width, 2) + pow(self.height, 2))}cm\n")

circle = Circle("red", True, 5)
square = Square("green", True, 4)
triangle = Triangle("Black", False, 4, 5)

circle.describe()
square.describe()
triangle.describe()