#!/usr/bin/python3
"""class Square"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        """class Square"""
        self.__size = size

    def area(self):
        """Calculate area of square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """property"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
