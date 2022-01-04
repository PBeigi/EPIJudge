from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    last = len(A) - 1
    i = m - 1
    j = n - 1
    for k in reversed(range(last+1)):
        if j >=0 and i >=0:
            a = A[i]
            b = B[j]
            if a > b:
                A[k]=A[i]
                i-=1
            if a <= b:
                A[k] = B[j]
                j-=1
        elif i>=0:
            A[k] = A[i]
            i-=1
        elif j>=0:
            A[k] = B[j]
            j-=1



def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
