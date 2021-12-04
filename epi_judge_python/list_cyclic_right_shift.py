from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if k == 0:
        return L
    len = 0
    it = L
    while it:
        len+=1
        it = it.next
    if len == 0:
        return L
    k = k % len

    dummy_head = ListNode()
    dummy_head.next = L
    ahead = dummy_head
    for _ in range(k):
        ahead = ahead.next
    previous = dummy_head
    while ahead and ahead.next:
        ahead = ahead.next
        previous = previous.next
    ahead.next = L
    tmp = previous.next
    previous.next = None
    return tmp















if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
