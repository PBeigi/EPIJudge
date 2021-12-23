from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    lo = 0
    hi = len(A) - 1
    while lo <= hi:
        mid_idx = lo + (hi-lo)//2
        mid = A[mid_idx]
        if k < mid:
            hi = mid_idx - 1
        if k == mid:
            if mid_idx == 0 or A[mid_idx-1] != k:
                return mid_idx
            if A[mid_idx-1] == k:
                hi = mid_idx - 1
        if k > mid:
            lo = mid_idx + 1
    return -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
