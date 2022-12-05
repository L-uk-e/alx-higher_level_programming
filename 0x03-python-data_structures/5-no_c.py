#!/usr/bin/python3

def no_c(my_string):
    word = my_string
    l = len(word)
    s = 0

    while s < l:
        if word[s] == 'c' or word[s] == 'C':
            word = word[:s] + word[s + 1:]
            l -= 1
        s += 1            

    return word
