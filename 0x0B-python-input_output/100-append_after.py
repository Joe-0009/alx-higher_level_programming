#!/usr/bin/python3
"""defines a function inserts line of text"""


def append_after(filename="", search_string="", new_string=""):
    """present a function that inserts a line of text to a file,
    after each line containing a specific string .

    Args:
        filename (str): files name
        search_string (str): the string to search for
        new_string (str): the string replacement
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)

        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(search_string)
        f.truncate()
