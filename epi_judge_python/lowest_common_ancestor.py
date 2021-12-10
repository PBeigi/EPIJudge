import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # def helper(root, node0, node1):
    #     if not root:
    #         return False
    #     if root is node0 or root is node1:
    #         return root
    #     right = helper(root.right, node0, node1)
    #     left = helper(root.left, node0, node1)
    #     if right and left:
    #         return root
    #     return right or left
    # res = helper(tree, node0, node1)
    # return res

    def helper(root, node0, node1):
        if not root:
            return False
            right = helper(root.right, node0, node1)
            left = helper(root.left, node0, node1)
            if right and left:
                return root



@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
