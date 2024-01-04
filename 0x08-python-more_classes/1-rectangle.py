#!/usr/bin/python3
"""A class Rectangle that defines a rectangle based on 0-rectangle.py"""


class Rectangle:
    """Defining a rectangle"""

    def __init__(self, width=0, height=0):
        """To initialize the class rectangle
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
        """To retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To retrieve height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """To set the attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
