#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    # max_key = []
    if a_dictionary is None:
        return None
    else:
        if len(a_dictionary) > 1:
            max_value = max(a_dictionary.values())
            for i in a_dictionary:
                if a_dictionary[i] == max_value:
                    return i
                else:
                    continue
        elif len(a_dictionary) == 1:
            for i in a_dictionary.keys():
                return i
