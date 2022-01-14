import collections
from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def merge_sorted_list(a, b):
    dummy_head = ListNode()
    tail = dummy_head
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    if a:
        tail.next = a
    if b:
        tail.next = b
    return dummy_head.next


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    if not L or not L.next:
        return L
    slow = L
    fast = L
    pre = slow
    while fast and fast.next:
        pre = slow
        fast = fast.next.next
        slow = slow.next
    pre.next = None
    return merge_sorted_list(stable_sort_list(L), stable_sort_list(slow))



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
