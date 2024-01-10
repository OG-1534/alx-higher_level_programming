#!/usr/bin/python3
"""
This module a function that prints a square with the character #
"""


def print_square(size):
    """Function that prints the square with the character #
    Args:
        size (int): length of the square
    Raises:
        TypeError: Size is float and < 0
        TypeError: Size must be >= 0
        ValueError: If size < zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(size):
            print("#", end="")
        print("")
