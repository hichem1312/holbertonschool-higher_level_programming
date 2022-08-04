#!/usr/bin/python3
"""dividing"""


def check_number(x):
    """function"""

    return type(x) is int or type(x) is float


def matrix_divided(matrix, div):
    """divide function"""

    if not (check_number(div)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])
    new_matrix = []
    for i in matrix:
        if len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")

        if not isinstance(i, list):
            raise TypeError(("matrix must be a matrix (list of lists) of integers/floats"))
        new_list = [round(elem / div, 2) for elem in i]
        new_matrix.append(new_list)

    return new_matrix
