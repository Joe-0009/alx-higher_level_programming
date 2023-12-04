#!/usr/bin/python3
"""function returns true or false"""


def is_same_class(obj, a_class):
    """ returns true of obj from a_class else false
    Args:
        obj (any): the object to check
        a_clas (type): the class to match the type of the object
    Returns:
        True if obj from a_class, false otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
