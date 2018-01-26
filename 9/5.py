from binary_tree_node import BinaryTreeNode

def sum_root_to_leaf(tree, partial_path_sum=0):
    if not tree: return 0

    partial_path_sum = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right: return partial_path_sum
    return (sum_root_to_leaf(tree.left, partial_path_sum) +
            sum_root_to_leaf(tree.right, partial_path_sum))

#      1
#    1   0
#       1


root = BinaryTreeNode(1)
assert sum_root_to_leaf(root) == 1
root.left = BinaryTreeNode(1)
assert sum_root_to_leaf(root) == 3
root.right = BinaryTreeNode(0)
assert sum_root_to_leaf(root) == 5
root.right.left = BinaryTreeNode(1)
assert sum_root_to_leaf(root) == 8
