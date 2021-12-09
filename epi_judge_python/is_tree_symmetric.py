from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def helper(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.data != right.data:
            return False
        left_res = helper(left.right, right.left)
        right_res = helper(left.left, right.right)
        return left_res & right_res
    if not tree:
        return True
    return helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
