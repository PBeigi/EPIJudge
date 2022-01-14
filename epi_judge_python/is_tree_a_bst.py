import collections

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def helper(root, res):
    # if not root:
    #     return
    # helper(root.left, res)
    # res.append(root.data)
    # helper(root.right, res)

    # if not root:
    #     return []
    # st = []
    # cur = root
    # while st or cur:
    #     while cur:
    #         st.append(cur)
    #         cur = cur.left
    #     cur = st.pop()
    #     if res and res[-1] > cur.data:
    #         return False
    #     res.append(cur.data)
    #     cur = cur.right
    # return True

    Value = collections.namedtuple('Value', ('node','min', 'max'))
    q = collections.deque([Value(node=root, min=float('-inf'), max=float('inf'))])

    while q:
        node, min, max = q.pop()
        if node:
            if not min <= node.data <= max:
                return False
            else:
                q.appendleft(Value(node=node.left, min=min, max=node.data))
                q.appendleft(Value(node=node.right, min=node.data, max=max))
    return True



def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    res = []
    return helper(tree, res)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
