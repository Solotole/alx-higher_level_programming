#!/usr/bin/python3
"""class inheritance with the public class attributes"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle declaration"""

    def __init__(self, width, height):
        """class Recytangle instantiation"""
        # self.__width = width
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        # super().integer_validator("height", height)
        # self.integer_validator("height", height)
        self.__height = height
