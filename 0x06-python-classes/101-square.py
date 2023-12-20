#!/usr/bin/python3
# 6-square.py by OG-1534
"""Module of my square"""


class Square:
    """class that defines a Square."""

    def __str__(self):
        """python to print the square to stdout"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation of square variables
        Args:
            size: length of square side
            position: location of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """to retrieve size of square
        Raises:
            TypeError: size is not an integer.
            ValueError: size is less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        """to set the size of the square
        Args:
            value: the size of the square
        Raises:
                TypeError: value is not an integer
                ValueError: value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """to retrieve position of the square
        Raises:
            TypeError: position not a tuple of 2 positive ints
        Returns: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """to set square position
        Args:
            value: tuple of 2 positive ints
        Raises:
                TypeError: not tuple of 2 positive ints
        Returns: position
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """computes the area of a square
        Returns: current square area
        """
        return (self.__size ** 2)

    def pos_print(self):
        """prints in stdout the square with character #"""
        posi = ""
        if not self.size:
            return "\n"
        for u in range(self.position[1]):
            posi += "\n"
        for u in range(self.size):
            for x in range(self.position[0]):
                posi += " "
            for k in range(self.size):
                posi += "#"
            posi += "\n"
        return posi

    def my_print(self):
        """prints the square."""
        print(self.pos_print(), end="")
