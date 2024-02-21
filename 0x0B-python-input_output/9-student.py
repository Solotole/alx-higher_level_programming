#!/usr/bin/python3
"""a class definition"""


class Student:
    """student representation"""
    def __init__(self, first_name, last_name, age):
        """class instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation"""
        return self.__dict__
