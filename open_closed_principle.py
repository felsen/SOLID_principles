"""
This is the example about open-closed principle.

Class, Function, or Method should be open for extension but closed for modification. Easy to add new features.

"""

from abc import ABC, abstractmethod

# Bad example


class Shape:

    def __init__(self, type):
        self.type = type

    def area(self, width, height, radius):
        if self.type == "Rectangle":
            return self.height * self.width
        elif self.type == "Square":
            return self.height * self.width
        elif self.type == "Circle":
            return 3.14 * (radius ** 2)


# Good Example

class Shape:

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    @abstractmethod
    def area(self):
        return self.height * self.width


class Square(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    @abstractmethod
    def area(self):
        return self.width * self.height


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    @abstractmethod
    def area(self):
        return 3.14 * ( radius ** 2 )

