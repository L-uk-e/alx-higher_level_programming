#!/usr/bin/python3

"""Describe a class"""


class Square:
    """This is a squre"""

    def __init__(self, size=0):
        """Initialize an instance of the square.

        Args:
            size (int): The length of the sides of the square.
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
