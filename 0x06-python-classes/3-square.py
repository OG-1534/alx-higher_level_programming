#!/usr/bin/python3
# 2-square.py by OG-1534
"""A class square that defines a square"""


class Square:
    """The class that represents the square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represents size of the defined square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Computes area of the square
        Returns: current square area
        """

        return (self.__size ** 2)
