#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        if len(row) == 0:
            print()
        for idx in range(len(row)):
            print("{:d}".format(row[idx]), end="")
            if idx == len(row) - 1:
                print()
            else:
                print(" ", end="")
