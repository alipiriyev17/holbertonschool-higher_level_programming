#!/usr/bin/python3
"""
Matrix division module
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix: list of lists of integers/floats
        div: number to divide by

    Returns:
        new matrix with divided values

    Raises:
        TypeError, ZeroDivisionError
    """

    # Check matrix structure
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check elements
    for row in matrix:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            # NaN check
            if isinstance(x, float) and x != x:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    # Check same row size
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(
                "Each row of the matrix must have the same size")

    # Check div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide matrix (handles inf correctly)
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            result = x / div
            if result == 0:
                result = 0.0
            new_row.append(round(result, 2))
        new_matrix.append(new_row)

    return new_matrix
