#!/usr/bin/python3

def multiple_returns(sentence):
    my_tuple = ()
    if sentence:
        my_tuple = len(sentence), sentence[0]
    else:
        my_tuple = 0, 'None'
    return my_tuple
