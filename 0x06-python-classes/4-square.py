#!/usr/bin/python3
# 3-square.py by OG-1534
"""A class square that defines a square"""


class Square:
    """The class representing the square"""

    def __init__(self, size=0):
        """To initialize the class square
        Args:
            size: represents the size of the defined square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """To retrieve the square size"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Compute square area
        Returns: current square area
        """

        return (self.__size ** 2)
