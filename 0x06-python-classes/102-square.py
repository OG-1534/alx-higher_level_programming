#!/usr/bin/python3
# 4-square.py by OG-1534
"""Module for my square"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0):
        """To create the square
        Args:
            size: size of square sides
        """
        self.__size = size

    @property
    def size(self):
        """"To retrieve size of square
        Raises:
            TypeError: size is not an integer
            ValueErrorr: size less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Compute square area
        Returns: current square area
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
