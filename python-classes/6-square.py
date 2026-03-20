#!/usr/bin/python3
"""Defines a square with size, position and printing"""


class Square:
    """Square class with size, position, area and printing"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with size and position"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using # with position"""
        if self.__size == 0:
            print()
            return

        # vertical spacing (y)
        for _ in range(self.__position[1]):
            print()

        # square printing
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
