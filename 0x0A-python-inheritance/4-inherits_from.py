#!/usr/bin/python3
"""sub class confirmation"""


def inherits_from(obj, a_class):
    """subclass confirmation method

    Retuens:
        return True if obj is an instance of a class or inherited
        and false otherwise
    """
    if issubclass(type(obj), a_class) is type(a_class):
        return True
    return False
