#!/usr/bin/pyhon3
def only_diff_elements(set_1, set_2):
    not_both = set_1 ^ set_2
    return not_both
