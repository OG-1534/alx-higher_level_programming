#!/usr/bin/python3
# 4-square.py by OG-1534
"""A class square that defines a square"""


class Square:
    """The class representing a square"""

    def __init__(self, size=0):
        """To initialize this class square
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
        """To retrieve the area of a square"""

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
        Computes square area
        Returns: current square area
        """

        return (self.__size ** 2)

    def my_print(self):
        """print the square with the character #"""

        if self.__size == 0:
            print()

        for x in range(self.__size):
            print("#" * self.__size)
