#!/usr/bin/python3
"""BaseGeometry"""


class BaseGeometry:
    """A class"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """rectangle"""
    def __init__(self, width, height):
        """rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """square"""
    def __init__(self, size):
        """square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"square"""
        return self.__size ** 2

    def __str__(self):
        """square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

