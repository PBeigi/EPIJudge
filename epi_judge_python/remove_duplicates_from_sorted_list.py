from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    it = cur = L
    while cur and it.next:
        if it.next.data == cur.data:
            it.next = it.next.next
        else:
            it = it.next
            cur = cur.next
    return L





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
