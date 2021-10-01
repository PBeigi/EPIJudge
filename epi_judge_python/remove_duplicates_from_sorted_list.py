from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:

    # cur = L
    # while cur:
    #     while cur.next and cur.next.data == cur.data:
    #         cur.next = cur.next.next
    #     cur = cur.next
    # return L
    # cur = L
    #
    # while cur:
    #     next_distinct = cur.next
    #     while next_distinct and next_distinct.data == cur.data:
    #         next_distinct = next_distinct.next
    #     cur.next = next_distinct
    #     cur = next_distinct
    # return L

    it = cur = L
    while cur and it.next:
        if it.next.data == cur.data:
            it.next = it.next.next
        else:
            it = it.next
            cur = it
    return L

    while cur and it.next:
        if it.next.data == cur.data:
            it = it.next
        else:
            cur.next = it.next
            cur = it.next
            it = cur
    return L







if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
