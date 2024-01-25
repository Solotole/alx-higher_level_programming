#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    max_key = []
    if a_dictionary is None:
        return None
    else:
        max_value = max(a_dictionary.values())
        for i in a_dictionary:
            if a_dictionary[i] == max_value:
                max_key.append(i)
                break
            else:
                continue
    return max_key[0]
