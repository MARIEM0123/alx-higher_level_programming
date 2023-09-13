#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_mat = matrix.copy()

    for i in range(len(matrix)):
        nw_mat[i] = list(map(lambda x: x**2, matrix[i]))

    return (nw_mat)
