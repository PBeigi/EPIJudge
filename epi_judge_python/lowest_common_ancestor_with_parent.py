import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import collections



def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    Status = collections.namedtuple('Status', ('found' , 'ancestor'))

    def helper(node, target, path):
        if node is target:
            return Status(found=True, ancestor=node)
        if node.parent is None:
            path.append(node)
            return Status(found=False, ancestor=None)
        path.append(node)
        return helper(node.parent, target, path)

    node0_path = []
    res0 = helper(node0, node1, node0_path)
    if res0.found:
        return res0.ancestor

    node1_path = []
    res1 = helper(node1, node0, node1_path)
    if res1.found:
        return res1.ancestor
    removed_nodes = []
    while node0_path and node1_path:
        a = node0_path.pop()
        removed_nodes.append(a)
        b = node1_path.pop()
        if a is not b:
            removed_nodes.pop()
            return removed_nodes.pop()










@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
