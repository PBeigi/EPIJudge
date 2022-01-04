from typing import List
from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    left = 0
    right = 0
    longest = 0
    most_recent_occurence = dict()

    while right < len(A):
        c = A[right]
        if c in most_recent_occurence:
            most_recent_idx = most_recent_occurence[c]
            if most_recent_idx >=left:
                longest = max(right - 1 - left + 1, longest)
                left = most_recent_idx + 1
        most_recent_occurence[c] = right
        right+=1
    return max(longest, len(A) - left)





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
