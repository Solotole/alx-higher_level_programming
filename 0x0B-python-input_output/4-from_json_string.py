#!/usr/bin/python3
"""json module"""
import json  # importing the json module


def from_json_string(my_str):
    """deals with json string coversion

    Args:
        my_str (str): json string to be converted to object

    Returns:
        object represented by the json string
    """
    return json.loads(my_str)
