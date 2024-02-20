#!/usr/bin/python3
"""class inheritance with the public class attributes"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle declaration"""

    def __init__(self, width, height):
        """class Recytangle instantiation"""
        # self.__width = width
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area method that returns area

        Returns:
            return the product if the sides-area
        """
        return self.__width * self.__height

    def __str__(self):
        """str magic method

        Returns:
            return a string
        """
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string

