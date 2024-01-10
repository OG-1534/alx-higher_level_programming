#!/usr/bin/python3
"""
This module has a function that add 2 integers
"""


def add_integer(a, b=98):
    """Returns an integer on addition of a and b
    Args:
        a: first argument
        b: second argument
    Returns:
        Sum of a and b
    Raises:
        TypeError: If a or b is  not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
