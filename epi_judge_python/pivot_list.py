import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    less_list = less_list_it = ListNode()
    equal_list = equal_list_it = ListNode()
    greater_list = greater_list_it = ListNode()
    it = l
    while it:
        if it.data == x:
            equal_list_it.next = it
            equal_list_it = equal_list_it.next
        elif it.data < x:
            less_list_it.next = it
            less_list_it = less_list_it.next
        else:
            greater_list_it.next = it
            greater_list_it = greater_list_it.next
        it = it.next
    greater_list_it.next = None
    equal_list_it.next = greater_list.next
    less_list_it.next = equal_list.next
    return less_list.next



def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
