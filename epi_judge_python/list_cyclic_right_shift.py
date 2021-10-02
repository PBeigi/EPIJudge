from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if k == 0 or not L:
        return L
    dummy = ListNode()
    dummy.next = L
    shifted_list = ListNode()
    end = dummy
    node_count = 0
    cur = dummy.next
    while cur:
        node_count+=1
        cur = cur.next
    k = k % node_count
    i = 0
    while end and i < k:
        end = end.next
        i+=1
    p = dummy
    while end and end.next:
        end = end.next
        p = p.next
    shifted_list.next = p.next
    head = shifted_list
    p.next = None

    while head and head.next:
        head = head.next
    head.next = dummy.next
    return shifted_list.next





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
