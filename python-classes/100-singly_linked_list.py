#!/usr/bin/python3
"""This module defines a node class."""


class Node:
    """Node class with data and next_node attributes."""
    def __init__(self, data, next_node=None):
        """Initializes node with data and next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Checks data attribute and sets it."""
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Retrieves next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Checks value and sets next_node."""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a SinglyLinkedList."""
    def __init__(self):
        """Simple instantiation."""
        self.__head = None

    def __str__(self):
        """Prints the entire list."""
        my_list = []
        current = self.__head
        while current is not None:
            my_list.append(str(current.data))
            current = current.next_node
        return '\n'.join(my_list)

    def sorted_insert(self, value):
        """Inserts a new node to the Singly Linked List."""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None
            and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
