from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    layers = len(square_matrix) // 2
    for layer in range(layers):
        start = layer
        end = len(square_matrix) - layer - 1
        for i in range(start, end):
            offset = i - start
            top = square_matrix[layer][i]
            # left to top
            square_matrix[layer][i] = square_matrix[end-offset][layer]
            # bottom to left
            square_matrix[end-offset][layer] = square_matrix[end][end-offset]
            # right to bottom
            square_matrix[end][end - offset] = square_matrix[i][end]
            # top to right
            square_matrix[i][end] = top

def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
