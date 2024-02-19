#!/usr/bin/python3
"""empty class representation"""


class BaseGeometry:
    """empty class"""
    def area(self):
        """raising exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validation of value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle declaration"""
    def __init__(self, width, height):
        """class Recytangle instantiation"""
        super().integer_validator("width", width)
        # super().integer_validator("height", height)
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
        # super().__init__(self.name, self.__height)
