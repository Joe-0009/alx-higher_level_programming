#!/usr/bin/python3
""" function that prints a square with the character #."""


def print_square(size):
    """prints a square


    Args:
        size (int): the size of the square
    Raises:
        TypeError: if size not integer or size is float and less than 0
        ValueError: if size < 0
    """
    if ((not isinstance(size, int) or (isinstance(size, float) and size < 0)):
        raise TypeError("ize must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
