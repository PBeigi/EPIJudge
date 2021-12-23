from typing import List

from test_framework import generic_test

import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    h = []
    arrays_iter = [iter(array) for array in sorted_arrays]
    for i, arr in enumerate(arrays_iter):
        el = next(arr, None)
        if el is not None:
            heapq.heappush(h, (el, i))
    res = []
    while h:
        el, arr_index = heapq.heappop(h)
        arr_it = arrays_iter[arr_index]
        res.append(el)
        next_el = next(arr_it, None)
        if next_el is not None:
            heapq.heappush(h, (next_el,arr_index))
    return res






if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
