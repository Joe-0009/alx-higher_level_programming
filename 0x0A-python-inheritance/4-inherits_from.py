#!/usr/bin/python3
"""Defines a fucntion that checks a class."""


def inherits_from(obj, a_class):
    """check if an object is an instance of that inherrited class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is directly or indirectly from a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
