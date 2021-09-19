from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    for i in reversed(range(len(perm) - 1)):
        if perm[i] < perm[i+1]:
            smallest = float('inf')
            smallest_idx = -1
            for j in range(i+1, len(perm)):
                if (perm[j] > perm[i]) and (perm[j] < smallest):
                    smallest = perm[j]
                    smallest_idx = j
            perm[i], perm[smallest_idx] = perm[smallest_idx], perm[i]
            return perm[:i+1] + sorted(perm[i+1:])
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
