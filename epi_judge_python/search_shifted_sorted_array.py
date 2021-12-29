from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    lo = 0
    hi = len(A) - 1
    while lo <= hi:
        mid_idx = lo + (hi-lo)//2
        mid = A[mid_idx]
        if mid < A[hi]:
            hi = mid_idx
        if mid > A[hi]:
            lo = mid_idx + 1
        if lo == hi:
            return lo



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
