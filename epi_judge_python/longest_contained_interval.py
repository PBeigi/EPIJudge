from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    s = set(A)
    longest = 0
    while s:
        number = s.pop()
        l = 1
        lower = number
        while lower - 1 in s:
            s.remove(lower-1)
            lower-=1
            l+=1

        upper = number
        while upper + 1 in s:
            s.remove(upper+1)
            upper+=1
            l+=1
        longest = max(longest,l)
    return longest




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
