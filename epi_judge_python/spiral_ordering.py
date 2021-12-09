from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if len(square_matrix) == 1:
        return [square_matrix[0][0]]
    layers = (len(square_matrix) + 1) // 2
    res = []
    for layer in range(layers):
        start = layer
        end = len(square_matrix) - layer - 1
        res+=square_matrix[layer][start:end]
        res+=[square_matrix[x][end] for x in range(start,end)]
        res+=[square_matrix[end][y] for y in reversed(range(start+1,end+1))]
        res+=[square_matrix[x][layer] for x in reversed(range(start+1, end+1))]
    if len(square_matrix) % 2 == 1:
        res.append(square_matrix[layer][layer])
    return res



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
