#!/usr/bin/python3
"""a singly linked list module"""


class Node:
    """"class node that defines a node"""

    def __init__(self, data, next_node=None):
        """node initialization with instantiation variables"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """to retrieve data attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """to set data attribute"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """to retrieve next_node attribute
        Returns: next_node
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """to set value of next_node attribute"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """class that defines a singly linked list"""

    def __init__(self):
        """Instantiation to singly linked list"""

        self.head = None

    def __str__(self):
        """print list in stdout"""

        printsll = ""
        position = self.head
        while position:
            printsll += str(position.data) + "\n"
            position = position.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """inserts a node in correct sorted position
        Args:
            value: value on the node
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        position = self.head
        while position.next_node and position.next_node.data < value:
            position = position.next_node
        if position.next_node:
            new.next_node = position.next_node
        position.next_node = new
