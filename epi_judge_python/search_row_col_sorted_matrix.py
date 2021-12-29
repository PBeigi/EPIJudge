from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    row = 0
    col = len(A[0]) - 1

    while row < len(A) and col >=0:
        num = A[row][col]
        if num < x:
            row+=1
        if num > x:
            col-=1
        if num == x:
            return True
    return False





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
