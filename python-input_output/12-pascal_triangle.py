#!/usr/bin/python3
"""Module that returns Pascal's triangle as a list of lists."""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing Pascal's triangle of n.

    If n <= 0, return an empty list.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        # Build the new row
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
