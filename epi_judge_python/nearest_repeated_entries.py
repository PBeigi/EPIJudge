from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    m = dict()
    global_min = float('inf')
    for i, s in enumerate(paragraph):
        if s in m:
            global_min = min(i - m[s], global_min)
        m[s] = i
    return global_min if global_min != float('inf') else - 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
