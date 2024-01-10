#!/usr/bin/python3
"""
This module has a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by div
    Args:
        matrix: A list of lists of integers or floats
        div: Number to be used for the division (must be a float or integer)
    Raises:
        TypeError: If matrix is not an int or float
        TypeError: If matrix row sizes are not same
        TypeError: If div is not a number (int or float)
        ZeroDivisionError: If div is equal to 0
    Returns:
        A new matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
