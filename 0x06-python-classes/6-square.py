#!/usr/bin/python3
# 5-square.py by OG-1534


class Square:
    """A class square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """To initialize the class square
        Args:
            size: size of square
            position: location of the square
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """"To retrieve the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """To retrieve position of the square
        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the squares's position
        Args:
            Value: tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Compute the area of square
        Returns: current square area
        """
        return (self.__size ** 2)

    def pos_print(self):
        """returns the position in spaces"""
        posi = ""
        if self.size == 0:
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
        """print the square with the character #"""
        print(self.pos_print(), end='')
