import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    def has_cycle(h):
        slow = fast = h
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                slow = h
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

    def overlap_no_cycles(h1,h2):
        while h1 and h1.next:
            h1=h1.next
        while h2 and h2.next:
            h2=h2.next
        if h1 is h2:
            return h1
        return None

    l0_root = has_cycle(l0)
    l1_root = has_cycle(l1)
    if not l0_root and not l1_root:
        return overlap_no_cycles(l0, l1)
    if (not l0_root and l1_root) or (l0_root and not l1_root):
        return None
    else:
        tmp = l0_root
        while tmp:
            tmp=tmp.next
            if tmp is l0_root or tmp is l1_root:
                break
        return tmp if tmp is l1_root else None



@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
