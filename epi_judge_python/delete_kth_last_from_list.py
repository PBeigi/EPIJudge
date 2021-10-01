from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummy = ListNode(next=L)
    last_node = dummy
    for _ in range(k):
        last_node = last_node.next
    p = dummy
    while last_node and last_node.next:
        last_node = last_node.next
        p = p.next
    p.next = p.next.next
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
