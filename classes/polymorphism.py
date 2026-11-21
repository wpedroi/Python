import math as m
from abc import ABC, abstractmethod

class Shape:
    def __init__(self, radios):
        self.radios = radios
    @abstractmethod
    def area(self):
        return self.radios ** 2


class Circle(Shape):
    def __init__(self, radios):
        self.radios = radios

    def area(self):
        return m.pi * self.radios ** 2

class Square(Shape):
    def __init__(self, radios):
        self.radios = radios

    def area(self):
        return self.radios


class Triangle(Shape):
    def __init__(self, radios):
        self.radios = radios

    def area(self):
        return self.radios


class pizza(Circle):
    def __init__(self, tappo, radios):
        self.tappo = tappo
        self.radios = radios
    def area(self):
        return shape.radios ** 2

shapes = [Circle(5), Square(4), Triangle(5), pizza("Peperoni", 3)]

for shape in shapes:
    print(f"{shape.area()}cm^2")