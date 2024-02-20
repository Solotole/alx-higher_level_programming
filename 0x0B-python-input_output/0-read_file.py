#!/usr/bin/python3
"""reading from a file"""


def read_file(filename=""):
    """function that reads from a file"""
    with open(filename) as file:
        lines = file.read()
        print("{0:s}".format(lines), end="")
