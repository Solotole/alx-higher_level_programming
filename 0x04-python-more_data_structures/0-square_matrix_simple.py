#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix != [[]]:
        new_matrix = [row[:] for row in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_matrix[i][j] = matrix[i][j] ** 2 
    else:
        new_matrix = martix
    return new_matrix
