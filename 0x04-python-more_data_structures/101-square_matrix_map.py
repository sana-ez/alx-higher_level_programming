#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lamda x: list(map(lamda y: y**2 x)), matrix)))
