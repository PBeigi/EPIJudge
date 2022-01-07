import collections
from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    l_by_val = collections.defaultdict(list)
    it = L
    while it:
        l_by_val[it.data].append(it)
        it = it.next
    dummy_head = ListNode()
    tail = dummy_head
    sorted_keys = sorted(l_by_val)
    i = 0
    while l_by_val:
        data = sorted_keys[i]
        i+=1
        values = l_by_val[data]
        for value in values:
            tail.next = value
            tail = tail.next
        del l_by_val[data]
        if len(l_by_val) == 0:
            tail.next = None
    return dummy_head.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
