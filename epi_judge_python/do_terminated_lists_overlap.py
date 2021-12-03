import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    l0_len = 0
    l1_len = 0
    l0_it = l0
    l1_it = l1
    if not l0 or not l1:
        return None
    while l0_it and l0_it.next:
        l0_it = l0_it.next
        l0_len+=1
    while l1_it and l1_it.next:
        l1_it = l1_it.next
        l1_len+=1
    if l0_it is l1_it:
        diff = abs(l0_len - l1_len)
        if l0_len > l1_len:
            for _ in range(diff):
                l0 = l0.next
        elif l1_len > l0_len:
            for _ in range(diff):
                l1 = l1.next
        while l1 is not l0:
            l1 = l1.next
            l0 = l0.next
        return l1
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
