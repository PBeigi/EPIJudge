from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L
    even_head = ListNode()
    even_it =even_head
    odd_head = ListNode()
    odd_it = odd_head
    it = L
    i = 0
    while it:
        if i%2 == 0:
            even_it.next = it
            even_it = even_it.next
        else:
            odd_it.next = it
            odd_it = odd_it.next
        it = it.next
        i+=1
    odd_it.next = None
    even_it.next = odd_head.next
    return even_head.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
