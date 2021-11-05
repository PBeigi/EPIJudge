from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L or k == 0:
        return L
    it = L
    count = 1
    while it.next:
        count+=1
        it = it.next
    it.next = L
    k = k % count
    jumps = count - k
    last = L
    for _ in range(jumps-1):
        last = last.next
    res = last.next
    last.next = None
    return res












if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
