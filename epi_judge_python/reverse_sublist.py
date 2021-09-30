from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummy = ListNode(next=L)
    p = dummy
    for _ in range(start-1):
        p=p.next
    s = p.next

    for _ in range(finish-start):
        t = s.next
        s.next = t.next
        t.next = p.next
        p.next = t
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
