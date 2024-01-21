#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    else:
        new_tuple = ()
        length = len(sentence)
        character = sentence[0]
        new_tuple = length, character
    return new_tuple
