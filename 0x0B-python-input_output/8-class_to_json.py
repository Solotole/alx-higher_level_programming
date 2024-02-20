#!/usr/bin/python3
"""class json"""
import json  # import the json module


def class_to_json(obj):
    """function that returns json string

    Args:
        obj (object): object for serialization

    Returns:
        return dictionary of object obj
    """
    return obj.__dict__
