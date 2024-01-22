#!usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    first = tuple_a[0] + tuple_b[0]
    second = tuple_a[1] + tuple_b[1]
    new_tuple = first, second
    return new_tuple
