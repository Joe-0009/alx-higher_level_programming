#!/usr/bin/python3
"""function returns true or false"""


def is_same_class(obj, a_class):
    """ returns true of obj from a_class else false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
