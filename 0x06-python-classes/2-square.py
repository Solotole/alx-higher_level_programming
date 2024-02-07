#!/usr/bin/python3

"""Define class Square"""


class Square:
    """Square representant"""

    def __init__(self, size=0):
        """Initialize square.

        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
