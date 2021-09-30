import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    i = l0
    count0 = 0
    j = l1
    count1 = 0
    while i and i.next:
        count0 += 1
        i = i.next
    while j and j.next:
        count1 += 1
        j = j.next
    if i is j:
        i = l0
        j = l1
        diff = abs(count0 - count1)
        if count0 > count1:
            while diff:
                i = i.next
                diff -= 1
        elif count1 > count0:
            while diff:
                j = j.next
                diff -= 1
        while i is not j:
            i = i.next
            j = j.next
        return i
    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
