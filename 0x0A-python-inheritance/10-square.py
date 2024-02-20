#!.usr/bin/python3
"""class depicting multi level inheitance"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class represetation"""
    def __init__(self, size):
        """class square instantiation

        Size (int): size of the square side
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
