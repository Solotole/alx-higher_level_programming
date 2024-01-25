#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    max_key = ''
    if a_dictionary is None:
        return None
    else:
        max_value = max(a_dictionary.values())
        max_key = list(filter(lambda x : a_dictionary[x] == max_value, a_dictionary))

    return max_key[0]
