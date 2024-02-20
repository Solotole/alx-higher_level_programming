#!.usr/bin/python3
"""class depicting multi level inheitance"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class represetation"""
    def __init__(self, size):
        """class square instantiation

        Size (int): size of the square side
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method

        Returns:
            return area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """the str method

        Returns:
            return a string
        """
        base = Square.__bases__
        string = "[" + str(base[0].__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
