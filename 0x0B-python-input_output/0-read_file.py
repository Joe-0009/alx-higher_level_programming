#!/usr/bin/python3
"""Defines text files read."""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout."""

    with my_file = open('workfile', 'r', encoding="utf-8") as line:
        print(my_file)
