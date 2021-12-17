from typing import List

from test_framework import generic_test

import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    h = []
    for file in sorted_arrays:
        for time in file:
            heapq.heappush(h, time)
    res = []
    while h:
        res.append(heapq.heappop(h))
    return res



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
