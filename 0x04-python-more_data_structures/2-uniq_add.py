#!/usr/bin/python3

def uniq_add(my_list=None):
    if my_list is None:
        my_list = []

    unique_elements = set(my_list)
    
    total = sum(unique_elements)

    return total

