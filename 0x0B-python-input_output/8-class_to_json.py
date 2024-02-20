#!/usr/bin/python3
"""class json"""
import json  # import the json module


def class_to_json(obj):
    """function that returns json string

    Args:
        obj (object): object for serialization

    Returns:
        return a serialized object
    """
    return (obj.__dict__)
