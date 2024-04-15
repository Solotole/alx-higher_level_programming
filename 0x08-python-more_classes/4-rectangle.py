#!/usr/bin/python3
"""this a class rectangle"""


class Rectangle:
    """rectangle representation"""

    def __init__(self, width=0, height=0):
        """object/class instantiation

        Args:
            width (int): width of the rectangle
            height (int): heigth of the recatngle
        """
        self.__height = height
        self.__width = width

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
        self.__width = value

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
        self.__height = value

    def area(self):
        """area claculating area of rectangle

        Returns:
            return area of the rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """perimeter method

        Returns:
            return perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height + 2 * self.__width)

    def __str__(self):
        """str method

        Returns:
            return a list of characters # and \n
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        hash = []
        for i in range(self.__height):
            [hash.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                hash.append('\n')
        return ("".join(hash))

    def __repr__(self):
        """string representation of the class

        Returns:
            return formal string instance represenation
        """
        return f"{type(self).__name__}({self.__width}, {self.__height})"
