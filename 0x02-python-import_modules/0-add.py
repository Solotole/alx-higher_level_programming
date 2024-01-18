#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    first_value = 1
    second_value = 2
    sum = add(first_value, second_value)
    print("{0:d} + {1:d} = {2:d}".format(first_value, second_value, sum))
