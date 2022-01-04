import collections
import functools
from typing import List

from epi_judge_python_solutions.test_framework.test_failure import TestFailure
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:
    keyword_to_idx = {k:i for i, k in enumerate(keywords)}

    latest_occurance = [-1] * len(keywords)
    shortest_subarray_len = [float('inf')] * len(keywords)
    res = Subarray(start=-1, end=-1)
    shortest = float('inf')

    for i, p in enumerate(paragraph):
        if p in keyword_to_idx:
            keyword_idx = keyword_to_idx[p]
            if keyword_idx == 0:
                shortest_subarray_len[keyword_idx] = 1
            elif shortest_subarray_len[keyword_idx-1] != float('inf'):
                distance_to_previous = i - latest_occurance[keyword_idx-1]
                shortest_subarray_len[keyword_idx] = distance_to_previous + shortest_subarray_len[keyword_idx-1]
            latest_occurance[keyword_idx] = i
            if keyword_idx == len(keywords) - 1 and shortest_subarray_len[-1] < shortest:
                shortest = shortest_subarray_len[-1]
                res = Subarray(i - shortest + 1, i)
    return res


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure('Not all keywords are in the generated subarray')
        if para_idx >= len(paragraph):
            raise TestFailure('Subarray end index exceeds array size')
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_all_values.py',
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
