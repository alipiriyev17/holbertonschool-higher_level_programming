#!/usr/bin/env python3
"""
Module that demonstrates abstract classes and duck typing
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter"""
        pass


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return area of circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints area and perimeter of any shape
    Uses duck typing (no isinstance check)
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
