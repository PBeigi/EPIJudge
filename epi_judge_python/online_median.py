from typing import Iterator, List

from test_framework import generic_test

import heapq

def online_median(sequence: Iterator[int]) -> List[float]:
    minheap = []
    maxheap = []
    res = []
    for num in sequence:
        heapq.heappush(maxheap, -heapq.heappushpop(minheap, num))

        if len(maxheap) > len(minheap):
            heapq.push(minheap, -heapq.heappop(maxheap))
        if len(minheap) == len(maxheap):
            res.append((minheap[0] - maxheap[0]) / 2)
        else:
            res.append(minheap[0])
    return res



def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
