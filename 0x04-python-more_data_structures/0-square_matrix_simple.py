#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        x = []
        for j in range(len(matrix[i])):
            x.append(matrix[i][j] ** 2)
        new_matrix.append(x)
    return new_matrix
