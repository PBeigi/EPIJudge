from typing import List

from test_framework import generic_test, test_utils

import heapq

def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    h = []
    res = []

    h.append((-A[0], 0))

    for _ in range(k):
        num, i = heapq.heappop(h)
        num = -num
        res.append(num)
        if 2 * i + 1 < len(A):
            heapq.heappush(h, (-A[2*i+1], 2*i+1))
        if 2 * i + 2 < len(A):
            heapq.heappush(h, (-A[2*i+2], 2*i+2))
    return res









if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
