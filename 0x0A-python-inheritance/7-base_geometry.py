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
