from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummy_head = ListNode()
    dummy_head.next = L
    front = dummy_head
    for _ in range(k):
        front = front.next
    previous = dummy_head
    while front and front.next:
        front = front.next
        previous = previous.next
    previous.next = previous.next.next
    return dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
