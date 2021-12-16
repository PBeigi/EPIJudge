import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
import collections

Status = collections.namedtuple('Status', ('node', 'next_index'))

def helper(preorder, index):
    cur = preorder[index]
    if cur is None:
        return Status(node=None, next_index=index+1)
    cur_node = BinaryTreeNode(cur)
    status = helper(preorder, index+1)
    cur_node.left = status.node
    status = helper(preorder, status.next_index)
    cur_node.right = status.node
    return Status(node=cur_node, next_index=status.next_index)


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    status = helper(preorder, 0)
    return status.node


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
