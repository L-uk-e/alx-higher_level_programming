#!/usr/bin/python3

"""Define a class square."""


class Square:
    """This is a square"""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The length of the side of the square.
        """
            self.size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """Get/Set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
