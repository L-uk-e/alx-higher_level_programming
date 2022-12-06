#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) < 1:
        return (len(sentence), None)
    my_tuple = (len(sentence), sentence[0])
    return my_tuple
