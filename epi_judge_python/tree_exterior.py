import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    if not tree:
        return []
    def get_left(root, left_res):
        if not root:
            return
        if root.left or root.right:
            left_res.append(root)
        get_left(root.left or root.right, left_res)

    def get_bottom(root, bottom_res):
        if not root:
            return
        if not root.left and not root.right and root is not tree:
            bottom_res.append(root)
        get_bottom(root.left, bottom_res)
        get_bottom(root.right, bottom_res)

    def get_right(root, right_res):
        if not root:
            return
        get_right(root.right or root.left, right_res)
        if (root.left or root.right):
            right_res.append(root)

    left_res = []
    bottom_res = []
    right_res = []
    get_left(tree.left, left_res)
    get_bottom(tree, bottom_res)
    get_right(tree.right, right_res)
    res = [tree] + left_res + bottom_res + right_res
    return res


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
