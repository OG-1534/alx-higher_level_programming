#!/usr/bin/python3
"""Function that checks objects against classes."""


def is_kind_of_class(obj, a_class):
    """Returns true if object is an instance
    of/or a class that inherited from specified class."""
    if isinstance(obj, a_class):
        return True
    return False
