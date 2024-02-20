#!/usr/bin/python3
"""JSON string"""
import json


def to_json_string(my_obj):
    """function to convert into json string

    Args:
        my_obj (obj): object to convert into json string

    Returns:
        return json string
    """
    return json.dumps(my_obj)
