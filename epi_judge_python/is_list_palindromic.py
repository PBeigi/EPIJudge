from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L:
        return True
    count = 0
    it = L
    while it:
        it = it.next
        count+=1
    if count == 1:
        return True
    second_half_head = L
    for _ in range((count+1)//2):
        second_half_head = second_half_head.next
    second_half = []
    while second_half_head:
        second_half.append(second_half_head)
        second_half_head = second_half_head.next
    first_half_it = L
    for _ in range(count//2):
        second_half_val = second_half.pop()
        if second_half_val.data != first_half_it.data:
            return False
        first_half_it = first_half_it.next
    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
