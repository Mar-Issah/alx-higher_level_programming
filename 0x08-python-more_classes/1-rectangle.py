#!/usr/bin/python3
"""Write imported module here"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """ "Initializes the rectangle

        Args:
            width: width of the rect
            height: height of the rect
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method of the width

        Returns: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for the width

        Args:
            value: width's value

        Raises:
            TypeError: if width is not an integer
            ValueError: if width less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method of the height

        Returns: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for the height

        Args:
            value: height value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
