#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
            self.size = size
            self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not type(value) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
        for x in range(self.size):
            for z in range(self.position[0]):
                if self.position[1] > 0:
                    print("_", end="")
                else:
                    print(" ", end="")
            for y in range(self.size):
                print("#", end="")
            print()
