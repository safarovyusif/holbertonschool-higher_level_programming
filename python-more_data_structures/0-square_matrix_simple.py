#!/usr/bin/python3
"""
0-square_matrix_simple.py
Function that computes the square value of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    """
    matrix: list of lists of integers
    Returns a new matrix where each value is the square of the input value.
    The original matrix is not modified.
    """
    return [[item * item for item in row] for row in matrix]
