#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal’s triangle of n.
    """
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    trig = [[1]]
    for i in range(1, n):
        row = [1]
        row.extend([res[i - 1][j - 1] + res[i - 1][j] for j in range(1, i)])
        row.append(1)
        res.append(row)

    return trig
