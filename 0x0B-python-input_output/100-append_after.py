#!/usr/bin/python3
"""search and update"""


def append_after(filename="", search_string="", new_string=""):
    """function that nserts a line of text to a file"""
    with open(filename, "r") as text_file:
        string = text_file.readlines()
    for i in range(len(string)):
        if search_string in string[i]:
            string.insert(i + 1, new_string)
    with open(filename, "w") as text_file:
        text_file.writelines(string)
