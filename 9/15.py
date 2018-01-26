from binary_tree_node import BinaryTreeNode
reconstruct = __import__('13')

def exterior_binary_tree(tree):
    def is_leaf(node):
        return not node.left and not node.right

    def left_boundary_and_leaves(subtree, is_boundary):
        if not subtree: return []
        return (([subtree] if is_leaf(subtree) or is_boundary else []) +
                left_boundary_and_leaves(subtree.left, is_boundary) +
                left_boundary_and_leaves(subtree.right, not subtree.left and is_boundary))

    def right_boundary_and_leaves(subtree, is_boundary):
        if not subtree: return []
        return (right_boundary_and_leaves(subtree.left, not subtree.right and is_boundary) +
                right_boundary_and_leaves(subtree.right, is_boundary) +
                ([subtree] if is_leaf(subtree) or is_boundary else []))

    return ([tree] + left_boundary_and_leaves(tree.left, True) +
            right_boundary_and_leaves(tree.right, True) if tree else [])


def create_output_list(L):
    return [l.data for l in L]

A = [314, 6, 271, 28, 0, 561, 3, 17, 6, 2, 1, 401, 641, 257, 271, 28]
tree = reconstruct.reconstruct_preorder([
    A[0], A[1], A[2], A[3], None, None, A[4], None, None, A[5], None, A[6],
    A[7], None, None, None, A[8], A[9], None, A[10], A[11], None, A[12],
    None, None, A[13], None, None, A[14], None, A[15], None, None])

assert create_output_list(exterior_binary_tree(tree)) == [314, 6, 271, 28, 0, 17, 641, 257, 28, 271, 6]
