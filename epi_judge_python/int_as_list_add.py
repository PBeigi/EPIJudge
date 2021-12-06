from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    result = result_it = ListNode()
    over = 0
    while L1 and L2:
        s = L1.data + L2.data + over
        over = s // 10
        v = s % 10
        result_it.next = ListNode(v)
        result_it = result_it.next
        L1 = L1.next
        L2 = L2.next
    if L1:
        while L1:
            s = L1.data + over
            over = s // 10
            v = s % 10
            result_it.next = ListNode(v)
            result_it = result_it.next
            L1 = L1.next
    if L2:
        while L2:
            s = L2.data + over
            over = s // 10
            v = s % 10
            result_it.next = ListNode(v)
            result_it = result_it.next
            L2 = L2.next
    if over:
        result_it.next = ListNode(over)
    return result.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
