#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j != len(matrix) - 1:
                    print("{0:d}".format(matrix[i][j]), end=" ")
                else:
                    print("{0:d}".format(matrix[i][j]))
    else:
        print("")
