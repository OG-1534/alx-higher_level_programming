#!/usr/bin/python3
"""A class Rectangle that defines a rectangle based on 1-rectangle.py"""


class Rectangle:
    """The class represents a rectangle"""

    def __init__(self, width=0, height=0):
        """To initialize this rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: width must be an integer
            ValueError: width is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """To retrieve the attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set the attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To retrieve the attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """To set the attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
