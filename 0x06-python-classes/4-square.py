#!/usr/bin/python3
"""class square definition"""


class Square:
    """square representation"""

    def __init__(self, size=0):
        """object instantiation.

            Args:
                size (int): size of square side
        """

        self.__size = size

    @property
    def size(self):
        """getter method definition.

            Returns:
                returns size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter method definition

        Args:
                value (int): value of the square side
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area method defintion

            Returns:
                returns area of the square
        """
        return self.__size ** 2
