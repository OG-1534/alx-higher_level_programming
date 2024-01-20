#!/usr/bin/python3
"""Module that defines a square instance"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor that initializes the square
        Args:
           size: size of square sides.
           x: x axis position.
           y: y axis position.
        Return:
           Always nothing.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Public method that returns a string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """Getter of the square size
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter of the square size
        Args:
           value: size assigned
        Return:
           Always Nothing
        """
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """Public method that assigns attributes to square instance
        Args:
           *args: arguments list.
           **kwargs: arguments dictionary.
        Return:
           Always nothing
        """
        dict_order = ['id', 'size', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """Public method that returns the dictionary
           representation of a Square instance.
        """
        dict_order = ['id', 'x', 'size', 'y']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
