#!/usr/bin/python3
"""class module goes here"""


class Node:
    """class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """this is the constructor

                              Args:
        data: data in the node
        next_node: next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This getter func returns the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """This setter func sets the data

         Raises:
          TypeError: if value is not an integer

        Args:
           value: value to set
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This getter func returns the data
        Returns:
            the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This setter func sets the node

         Raises:
          TypeError: if node is not an objet

        Args:
           value: value to set
        """
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This is a class Square that defines a SinglyLinkedList"""

    def __init__(self):
        """this is the constructor"""
        self.head = None

    # def __str__(self):
    #     """teach python to print my way
    #     Returns: the printed thing"""
    #     printsll = ""
    #     location = self.head
    #     while location:
    #         printsll += str(location.data) + "\n"
    #         location = location.next_node
    #     return printsll[:-1]

    # def sorted_insert(self, value):
    #     """insert in a sorted fashion
    #     Args:
    #         value: what the value will be on the node
    #     """
    #     new = Node(value)
    #     if not self.head:
    #         self.head = new
    #         return
    #     if value < self.head.data:
    #         new.next_node = self.head
    #         self.head = new
    #         return
    #     location = self.head
    #     while location.next_node and location.next_node.data < value:
    #         location = location.next_node
    #     if location.next_node:
    #         new.next_node = location.next_node
    #     location.next_node = new
