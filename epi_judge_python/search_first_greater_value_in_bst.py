from typing import Optional

from bst_node import BstNode
from test_framework import generic_test

def in_order_traversal(root, k, first_seen_so_far):
    if not root:
        return first_seen_so_far
    if k < root.data:
        return in_order_traversal(root.left, k, root)
    else:
        return in_order_traversal(root.right, k, first_seen_so_far)

def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    first_seen_so_far = None
    res = in_order_traversal(tree, k, first_seen_so_far)
    return res



def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
