#!/usr/bin/python3
def number_keys(a_dictionary):
    keys_count = 0
    keys_list = []
    if a_dictionary != {}:
        keys_list = list(a_dictionary)
        keys_count = len(keys_list)
    else:
        keys_count = 0
    return keys_count
