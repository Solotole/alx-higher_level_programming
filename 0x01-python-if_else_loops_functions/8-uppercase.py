#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        string = ord(str[i])
        if (string > 97 and string < 122) or (string):
            print("{0:c}".format(string - 32), end="")
        else:
            print("{0:c}".format(string))
