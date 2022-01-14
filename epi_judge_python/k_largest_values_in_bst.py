from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

def traverse(root, k , res):
    if not root:
        return
    traverse(root.right, k, res)
    if len(res) < k:
        res.append(root.data)
        traverse(root.left, k, res)

def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    res = []
    traverse(tree, k, res)
    return res



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
