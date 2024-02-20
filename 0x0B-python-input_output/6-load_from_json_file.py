#!/usr/bin/python3
"""reading from json file"""
import json  # importing json module


def load_from_json_file(filename):
    """function to creates object from json file

    Args:
        filename (str): json file to create object
        from

    Returns:
        return json object from a json file
    """
    with open(filename, "r") as jfile:
        line = jfile.read()
    return json.loads(line)
