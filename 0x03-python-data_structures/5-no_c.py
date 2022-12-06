#!/usr/bin/python3

def no_c(my_string):
    word = my_string
    length = len(word)
    s = 0

    while s < length:
        if word[s] == 'c' or word[s] == 'C':
            word = word[:s] + word[s + 1:]
            length -= 1
        s += 1

    return word
