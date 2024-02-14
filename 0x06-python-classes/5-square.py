#!/usr/bin/python3
"""this is a square representation"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """class initialization

            Args:
                size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """getter method

            Returns:
                return side of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter method

            Args:
                value (int): set value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method calculating are af square

            Returns:
                return area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """method that prints an output on stdout"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                if (j == self.__size - 1):
                    print("{0:s}".format('#'))
                else:
                    print("{0:s}".format('#'), end="")
