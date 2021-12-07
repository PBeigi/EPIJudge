import collections
from typing import List, Deque

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []
    res = []
    q: Deque[BinaryTreeNode] = collections.deque()
    q.append(tree)

    while len(q):
        cur_size = len(q)
        l = []
        for _ in range(cur_size):
            node = q.popleft()
            l.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(l)
    return res









if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
