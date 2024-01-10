#!/usr/bin/python3
"""Checks if object is an instance of a class that inherited."""


def inherits_from(obj, a_class):
    """ Args:
    obj (any): object to check.
    a_class (type): class to match the type of obj to

    Returns True if object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
