#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """append mode in use

    Args:
        filename (str): file to be appended text
        text (str): text to be appended

    Returns:
        return count of appended text
    """
    with open(filename, "a+") as file:
        count = file.write(text)
    return count
