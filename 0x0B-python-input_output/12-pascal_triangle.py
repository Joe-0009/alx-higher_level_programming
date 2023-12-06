#!/usr/bin/python3
"""presents pascale triangle"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j = 0 or j = i:
                row.append(1)
            else:
                left_upper = triangle[i - 1][j - 1]
                right_upper = triangle[i - 1][j]
                row.append(left_upper + right_upper)
        triangle.append(row)
    return triangle
