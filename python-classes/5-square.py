#!/usr/bin/python3
"""Defines a square with printing capability"""


class Square:
    """Square class with size, area and printing"""

    def __init__(self, size=0):
        """Initialize square with size"""
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using #"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)
