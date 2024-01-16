#!/usr/bin/python3
# fuction checking for lowercase character
def islower(c):
    character = ord(c)
    if character >= 97 and character <= 122:
        return True
    if character < 97 or character > 122:
        return False
