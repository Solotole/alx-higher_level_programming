#!/usr/bin/pyhton3

"""Define class Square"""

class Square:
    """Square representant"""
    def __init__(self, size=0):
        """Initialize square.

        Args:
            size (int): size of square
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
