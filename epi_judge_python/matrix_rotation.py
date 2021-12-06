from typing import List

from test_framework import generic_test

def rotate_90(point, l):
    i = point[0]
    j = point[1]
    return j, l- i - 1

def rotate_matrix(square_matrix: List[List[int]]) -> None:
    layers = (len(square_matrix) + 1) // 2
    n = len(square_matrix)
    for layer in range(layers):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = square_matrix[first][i]
            # left to up
            square_matrix[first][i] = square_matrix[last-offset][first]
            # bottom to left
            square_matrix[last-offset][first] = square_matrix[last][last-offset]
            # right to bottom
            square_matrix[last][last-offset] = square_matrix[i][last]

            # top to up
            square_matrix[i][last] = top


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
