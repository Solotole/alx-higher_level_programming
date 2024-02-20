#!/usr/bin/python3
"""write  file function"""


def write_file(filename="", text=""):
    """writing to a file

    Args:
        filename (str): file name to write into
        text (str): text to be writen

    Returns:
        return character count of writen text
    """
    with open(filename, "w") as file:
        characters = file.write(text)
    return characters
