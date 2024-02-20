#!/usr/bin/python3
"""saving json into file"""
import json  # importing json module


def save_to_json_file(my_obj, filename):
    """writing json string into a file

    Args:
        my_object (obj): object to be converted to json string
        filename (str): file to be saved into
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
