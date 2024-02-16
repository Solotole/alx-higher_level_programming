#!/usr/bin/python3
"""this a class rectangle"""


class Rectangle:
    """rectangle representation
    Attributes:
        number_of_instances (int): used to calculate number of instsnces
        print_symbol (any): symbol for string representation
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """object/class instantiation

        Args:
            width (int): width of the rectangle
            height (int): heigth of the recatngle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        character = '#'
        if self.__width == 0 or self.__height == 0:
            return ""
        hash = []
        for i in range(self.__height):
            [hash.append(character) for j in range(self.__width)]
            if i != self.__height - 1:
                hash.append('\n')
        return ("".join(hash))

    def __del__(self):
        """method that deletes an instance of the class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method responsible for compairing rectangles

        Args:
            rect_1 (object): first instance argument
            rect_2 (object): second instance argument

        Returns:
            returns bigest triangle based on area or rect_1 if equal
        """
        max_value = 0
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            max_value = rect_1
        elif rect_2.area() > rect_1.area():
            max_value = rect_2
        return max_value

    @classmethod
    def square(cls, size=0):
        """this is a class method

        Args:
            size (int): size of the new rectangle

        Returns:
            return new rectangle with all sides equal to size
        """
        if size != 0:
            width, height = size, size
        else:
            pass
        return cls(width, height)
