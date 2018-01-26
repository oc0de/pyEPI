from binary_tree_node import BinaryTreeNode

def reconstruct_preorder(preorder):
    def reconstruct_preorder_helepr(preorder_iter):
        subtree_key = next(preorder_iter)
        if subtree_key is None: return None

        left_subtree = reconstruct_preorder_helepr(preorder_iter)
        right_subtree = reconstruct_preorder_helepr(preorder_iter)

        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)

    return reconstruct_preorder_helepr(iter(preorder))

#  1
# N 2
#  N N
preorder = [1, None, 2, None, None]
result = reconstruct_preorder(preorder)
assert result.data == 1 and not result.left and result.right.data == 2
