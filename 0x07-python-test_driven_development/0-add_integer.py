#!/usr/bin/python3

"""Defines the add_integer function"""


def add_integer(a, b=98):
    """Adds the two values given as arguments and returns integer of the result.
    Float arguments are typecast into int
    Any other type provided for argument raises a TypeError.
    Raises:
        TypeError: If either of a or b is anyother type apart from int and float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
