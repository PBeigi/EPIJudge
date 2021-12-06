from list_node import ListNode
from test_framework import generic_test

def reverse_list(head):
    previous = None
    it = head
    while it:
        tmp = it.next
        it.next = previous
        previous = it
        it = tmp
    return previous


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L:
        return True
    slow = fast = L
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    rev = reverse_list(slow)
    it = L
    while it and rev:
        if it.data != rev.data:
            return False
        it = it.next
        rev = rev.next
    return True




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
