#!/usr/bin/python3
"""Defines a class-checking function."""


def is_kind_of_class(obj, a_class):
    """check if an object from a calsss or the superclass.

    Args:
        obj (any): the object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if obj from a_class else returns False.
    """
    if isinstance(obj, a_class):
        return True
    return False
