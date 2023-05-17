#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda newMatrix: list(map(lambda x: x**2, newMatrix)), matrix))
