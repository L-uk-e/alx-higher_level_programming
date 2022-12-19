#!/usr/bin/python3

def no_c(my_string):
    word = ""

    for w in my_string:
        if w != "c" and w != "C":
            word = word + w
    return word
