#!/usr/bin/python3
"""A class MyList that inherits from list."""


class MyList(list):
    """This is a subclass of the class list."""

    def print_sorted(self):
        """Prints the list sorted ascending."""
        print(sorted(self))
