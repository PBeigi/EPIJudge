from typing import List

from test_framework import generic_test

import heapq

def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    i=0
    j=1
    m = dict()
    index = 0
    increasing = True
    while j < len(A):
        if j < len(A) and A[j] >= A[j-1] and increasing:
            j+=1
        elif increasing:
            m[index] = A[i:j]
            i = j
            j = j + 1
            increasing = False
            index+=1

        if j < len(A) and  A[j]<= A[j-1] and not increasing:
            j+=1
        elif not increasing:
            m[index] = A[i:j]
            i = j
            j = j + 1
            increasing = True
            index+=1
    m[index] = A[i:]

    h = []
    for index, arr in m.items():
        if index % 2 == 0 and len(arr):
            heapq.heappush(h, (arr[0], index))
            m[index] = arr[1:]
        elif index % 2 == 1 and len(arr):
            heapq.heappush(h, (arr[-1], index))
            m[index] = arr[:-1]

    res = []
    while h:
        v, index = heapq.heappop(h)
        res.append(v)
        if len(m[index]):
            if index % 2 == 0:
                heapq.heappush(h, (m[index][0], index))
                m[index] = m[index][1:]
            else:
                heapq.heappush(h, (m[index][-1], index))
                m[index] = m[index][:-1]
    return res









if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
