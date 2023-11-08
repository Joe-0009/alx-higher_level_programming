#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square = []

    if matrix is None:
        return square
    for row in matrix:
        row = [element ** 2 for element in row]
        square.append(row)

    return square
