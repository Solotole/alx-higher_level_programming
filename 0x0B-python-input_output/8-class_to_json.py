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
    data = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            data[attr] = value
    return data
