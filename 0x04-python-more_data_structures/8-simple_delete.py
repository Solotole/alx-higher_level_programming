#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary != {} and key != "":
        if key in a_dictionary:
            del a_dictionary[key]
        else:
            pass
    else:
        pass
    return a_dictionary
