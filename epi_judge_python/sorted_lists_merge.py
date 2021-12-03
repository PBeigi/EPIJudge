from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    res = ListNode()
    p = res
    while L1 and L2:
        if L1.data < L2.data:
            p.next = L1
            p = p.next
            L1 = L1.next
        elif L2.data < L1.data:
            p.next = L2
            p = p.next
            L2 = L2.next
        else:
            p.next = L1
            p = p.next
            L1 = L1.next
            p.next = L2
            p = p.next
            L2 = L2.next
    if L1:
        p.next = L1
    if L2:
        p.next = L2
    return res.next




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
