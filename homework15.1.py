import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_square = self.get_square() + other.get_square()
        side = math.sqrt(new_square)
        return Rectangle(round(side), math.ceil(new_square / round(side)))

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_square = self.get_square() * n
        side = math.sqrt(new_square)
        return Rectangle(round(side), math.ceil(new_square / round(side)))

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"
