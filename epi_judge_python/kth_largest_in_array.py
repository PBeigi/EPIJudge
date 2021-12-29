from typing import List

from test_framework import generic_test
import heapq
import random

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    def partition_around_pivot(pivot_index, left, right):
        pivot = A[pivot_index]
        new_pivot_index = left
        A[pivot_index], A[right] = A[right], A[pivot_index]

        for i in range(left, right+1):
            if A[i] >= pivot:
                A[new_pivot_index], A[i] = A[i], A[new_pivot_index]
                new_pivot_index+=1
        return new_pivot_index - 1

    left = 0
    right = len(A) - 1
    while left < right:
        pivot_idx = random.randint(left, right)
        pivot_value = A[pivot_idx]
        new_pivot_idx = partition_around_pivot(pivot_idx, left, right)

        if new_pivot_idx >= k - 1:
            right = new_pivot_idx
        else:
            left = new_pivot_idx + 1
    return A[left]




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
