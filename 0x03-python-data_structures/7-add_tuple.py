#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 1 and len(tuple_b) < 1:
        first = 0
    elif len(tuple_a) < 1:
        first = tuple_b[0]
    elif len(tuple_b) < 1:
        first = tuple_a[0]
    else:
        first = tuple_a[0] + tuple_b[0]

    if len(tuple_a) < 2 and len(tuple_b) < 2:
        second = 0
    elif len(tuple_a) < 2:
        second = tuple_b[1]
    elif len(tuple_b) < 2:
        second = tuple_a[1]
    else:
        second = tuple_a[1] + tuple_b[1]

    my_tuple = (first, second)

    return my_tuple
