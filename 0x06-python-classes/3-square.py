#!/usr/bin/python3
"""
    defining class Square
"""


class Square:
    """Square representation"""
    def __init__(self, size=0):
        """class instantiation
        Args:
            size (int): size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area method definition

        Returns:
            area of of square
        """
        return self.__size ** 2
