from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def helper(root, remaining):
    if not root:
        return False
    if not root.right and not root.left and remaining - root.data == 0:
        return True
    right = helper(root.right, remaining - root.data)
    if right:
        return True
    left = helper(root.left, remaining - root.data)
    if left:
        return True
    return False


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    return helper(tree, remaining_weight)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
