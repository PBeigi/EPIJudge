from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    Status = collections.namedtuple('Status', ('balanced', 'height'))

    def is_balanced(root):
        if not root:
            status = Status(True, 0)
            return status
        left_status = is_balanced(root.left)
        right_status = is_balanced(root.right)
        if not left_status.balanced or not right_status.balanced:
            return Status(False, 1 + max(left_status.height, right_status.height))
        else:
            balanced = True if abs(left_status.height - right_status.height) <= 1 else False
            return Status(balanced, 1 + max(left_status.height, right_status.height))

    status = is_balanced(tree)
    return status.balanced




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
