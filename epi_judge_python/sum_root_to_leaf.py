from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binToDec(b):
    res = 0
    for v in b:
        res = res*2 + v
    return res


def helper(root, path):
    if not root:
        return 0
    path.append(root.data)
    if not root.left and not root.right:
        res = binToDec(path)
    else:
        res = helper(root.right, path) + helper(root.left, path)
    path.pop()
    return res


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    path = []
    res = helper(tree, path)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
