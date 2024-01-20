#!/usr/bin/python3
"""Module that defines a class rectangle (modules.rectangle)"""
from models.base import Base


class Rectangle(Base):
    """Defines a class rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method that init values for a rectangle object
        Args:
           width: width size
           height: height size
           x: x variable
           y:  y variable
        Return:
           Always nothing
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getter and setter of width
    @property
    def width(self):
        """Getter the width size
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter the width size
        Args:
           value: size width is assigned
        Return:
           Always Nothing
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    # Getter and setter of height
    @property
    def height(self):
        """Getter of height size
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of height size
        Args:
           value: size height is assigned
        Return:
           Always Nothing
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    # Getter and setter for x variable
    @property
    def x(self):
        """Getter of the variable x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of the variable x
        Args:
           value: value x variable is assigned
        Return:
           Always Nothing
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # Getter and setter for y variable
    @property
    def y(self):
        """Getter of the varialble y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of the variable y
        Args:
           value: value that y variable is assigned
        Return:
           Always Nothing
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Public method that returns the area of the rectangle instance
        Args:
           No arguments
        Return:
           Area value of the rectangle instance
        """
        return self.width * self.height

    def display(self):
        """Public method that prints in stdout
           Rectangle instance with the character #
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + self.width * '#')

    def __str__(self):
        """Update the Class Rectangle by overriding str method
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """Public method that assigns an argument to each attribute
        Args:
           *args: arguments list
           **kwargs: arguments dictionary
        Return:
           Always nothing
        """
        dict_order = ['id', 'width', 'height', 'x', 'y']
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
        """Public method that returns a dictionary with
            of the object attributes.
        """
        dict_order = ['x', 'y', 'id', 'height', 'width']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
