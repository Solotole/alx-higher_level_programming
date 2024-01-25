#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        if key in a_dictionary:
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value
    else:
        pass
    return a_dictionary
