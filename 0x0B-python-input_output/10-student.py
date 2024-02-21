#!/usr/bin/python3
"""a class definition"""


class Student:
    """student representation"""
    def __init__(self, first_name, last_name, age):
        """class instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation

        Args:
            attrs (list): list of attributes
        """
        if (type(attrs) == list and 
                all(type(value) == str for value in attrs)):
            return (a: getattr(self, a) for a in attrs if hasattr(self, a))
        return sel.__dict__

