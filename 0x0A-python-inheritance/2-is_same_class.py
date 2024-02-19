#!/usr/bin/python3
"""module to confirm for an instance"""


def is_same_class(obj, a_class):
    """instance of a class
    
    Args:
        obj (int): value to be tested of its type
        a_class (class): class to be checked against the obj

    Returns:
        return True if it is an instance and Flase otherwise
    """
    return type(obj) is  a_class
