#!/usr/bin/python3
"""
Matrix division module
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    """

    # Matrix structure check
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Elements check (including NaN)
    for row in matrix:
        for x in row:
            if not isinstance(x, (int, float)) or \
               (isinstance(x, float) and x != x):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    # Same row size check (IMPORTANT FIX)
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("matrix must have each row with the same size")

    # div check
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Division
    return [[round(x / div, 2) for x in row] for row in matrix]
