from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L
    even_list = ListNode()
    even_list_it = even_list
    odd_list = ListNode()
    odd_list_it = odd_list
    num = 0
    it = L
    while it:
        if num % 2 == 0:
            even_list_it.next = it
            even_list_it = even_list_it.next
        elif num%2 == 1:
            odd_list_it.next = it
            odd_list_it = odd_list_it.next
        num+=1
        it = it.next
    odd_list_it.next = None
    even_list_it.next = odd_list.next
    return even_list.next




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
