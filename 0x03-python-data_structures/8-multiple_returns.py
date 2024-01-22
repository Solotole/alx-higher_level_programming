#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = ()
    if len(sentence) == 0:
        new_tuple = 0, None
    else:
        length = len(sentence)
        character = sentence[0]
        new_tuple = length, character
    return new_tuple
