from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    max_cur_reach = 0
    i=0
    while i < len(A) and i <=max_cur_reach:
        max_cur_reach = max(max_cur_reach, A[i]+i, max_cur_reach)
        i+=1
    return max_cur_reach >= len(A)-1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
