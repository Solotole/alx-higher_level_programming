#!/usr/bin/python3
"""this a class rectangle"""


class Rectangle:
    """rectangle representation"""

    def __init__(self, width=0, height=0):
        """object/class instantiation

        Args:
            width (int): width of the rectangle
            heigth (int): heigth of the recatngle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter class method

            Returns:
                return width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """the setter method

        Args:
            value (int): integer value to be set as width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """height getter method

            Returns:
                return height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method

        Args:
            value (int): value to be sett as height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
