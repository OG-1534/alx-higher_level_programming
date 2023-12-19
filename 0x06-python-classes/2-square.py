#!/usr/bin/python3
# 1-square.py by OG-1534
"""A class square that defines a square"""


class Square:
    """A class representing a square"""

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
