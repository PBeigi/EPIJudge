import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    table = collections.Counter(keywords)
    missing = len(table)
    start = 0
    end = 0
    shortest_sub = Subarray(start=0, end=float('inf'))
    while end < len(paragraph):
        word = paragraph[end]
        if word in table:
            table[word] -= 1
            if table[word] == 0:
                missing -= 1
        while missing == 0:
            if (end - start) < (shortest_sub.end - shortest_sub.start):
                shortest_sub = Subarray(start=start, end=end)
            word = paragraph[start]
            if word in table:
                table[word] += 1
                if table[word] == 1:
                    missing += 1
            start += 1
        end += 1
    return shortest_sub


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
