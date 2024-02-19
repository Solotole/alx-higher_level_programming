#!/usr/bin/python3
"""module to confirm for an instance"""


def is_same_class(obj, a_class):
    """instance of a class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
