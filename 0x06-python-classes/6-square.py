#!/usr/bin/python3
"""this is a square representation"""


class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):
        """class initialization

            Args:
                position (tuple): tuple for manipulating display
                size (int): size of the square
        """
        self.__position = position
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

    @property
    def position(self):
        """position tuple getter

        Returns:
            return the positon attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter method for the position attribute

            Args:
                value (tuple): tuple argument to set for the position tuple
        """
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """method that prints an output on stdout"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            if self.__position[1] <= 0 or self.__position[0] == self.__position[1]:
                for k in range(self.__position[0]):
                    print(' ', end="")
            for j in range(self.__size):
                if (j == self.__size - 1):
                    print("{0:s}".format('#'))
                else:
                    print("{0:s}".format('#'), end="")
