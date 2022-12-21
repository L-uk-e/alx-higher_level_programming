#!/usr/bin/python3

"""Define a class square."""
class Square:
    """This is the square"""

    def __init__(self, size=0):
        """Initialize an instance of the square.

        Args:
            size (int): The length of the sides of the square.
        """
        self.size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """Get/Set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Represent the square using '#' character."""
        if self.size == 0:
            print()
        for x in range(self.size):
            for y in range(self.size):
                print("#", end="")
            print()
