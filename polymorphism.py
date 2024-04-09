import math

class Form():

    def area(self):
        pass

class Square(Form):

    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Triangle(Form):

    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base * self.height) / 2

class Circle(Form):

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

side = input('Digite o valor do lado: ')
square = Square(int(side))
print(square.area())

base = input('Digite o valor da base: ')
height = input('Digite o valor da altura: ')
triangle = Triangle(int(base), int(height))
print(triangle.area())

radius = input('Digite o valor do raio: ')
circle = Circle(int(radius))
print(circle.area())