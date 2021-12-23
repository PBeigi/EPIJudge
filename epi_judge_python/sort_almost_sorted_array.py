from typing import Iterator, List

from test_framework import generic_test

import heapq

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    h = []
    for _ in range(k+1):
        v = next(sequence, None)
        if v is not None:
            heapq.heappush(h, v)
        else:
            break

    res = []
    while h:
        res.append(heapq.heappop(h))
        v = next(sequence, None)
        if v is not None:
            heapq.heappush(h, v)
    return res



def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
