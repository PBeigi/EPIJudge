from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    HeightWithBalancedStatus = collections.namedtuple('HeightWithBalancedStatus', ('height', 'balanced'))

    def helper(root):
        if not root:
            return HeightWithBalancedStatus(-1, True)
        left = helper(root.left)
        if not left.balanced:
            return HeightWithBalancedStatus(-1, False)
        right = helper(root.right)
        if not right.balanced:
            return HeightWithBalancedStatus(-1, False)
        if abs(left.height - right.height) > 1:
            return HeightWithBalancedStatus(-1, False)
        return HeightWithBalancedStatus(1+max(right.height, left.height), True)


    return helper(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
