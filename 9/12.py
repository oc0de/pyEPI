from binary_tree_node import BinaryTreeNode

def binary_tree_from_preorder_inorder(preorder, inorder):
    node_to_inorder_idx = {data:i for i, data in enumerate(inorder)}

    def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start: return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
                preorder[preorder_start],
                binary_tree_from_preorder_inorder_helper(
                    preorder_start + 1, preorder_start + left_subtree_size + 1,
                    inorder_start, root_inorder_idx),
                binary_tree_from_preorder_inorder_helper(
                    preorder_start + left_subtree_size + 1, preorder_end,
                    root_inorder_idx + 1, inorder_end))

    return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0, len(inorder))

res = binary_tree_from_preorder_inorder([1], [1])
assert res.data == 1

res = binary_tree_from_preorder_inorder([2, 1], [1, 2])
assert res.data == 2 and res.left.data == 1 and not res.right
