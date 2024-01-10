#!/usr/bin/python3
"""Function that checks obect and class"""


def is_same_class(obj, a_class):
    """Checks if object is an instance of a class,
    Returns true if object is an instance of the
    class, otherwise false"""
    return (type(obj) == a_class)
