#!/usr/bin/python3

def best_score(a_dictionary):
    max_ = 0
    for score in a_dictionary:
        if score > max_:
            max_ = score
    return a_disctionary[max_]
