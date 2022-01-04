from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    # citations.sort()
    # h_index = float('-inf')
    # i = len(citations) - 1
    # count = 0
    # while i >=0:
    #     count +=1
    #     if citations[i] >= count:
    #         h_index = max(h_index, count)
    #     i-=1
    # return h_index if h_index != float('-inf') else 0
    citations.sort()
    count = len(citations)
    for num in citations:
        if num < count:
            count-=1
    return count







if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
