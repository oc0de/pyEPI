from binary_tree_node import BinaryTreeNode

def has_path_sum(tree, remaining_weight):
    if not tree: return False
    if not tree.left and not tree.right: return remaining_weight == tree.data
    return (has_path_sum(tree.left, remaining_weight - tree.data) or
            has_path_sum(tree.right, remaining_weight - tree.data))

#      3
#    2   5
#  1    4 6

tree = BinaryTreeNode(3)
assert has_path_sum(tree, 3)
tree.left = BinaryTreeNode(2)
assert has_path_sum(tree, 5)
tree.right = BinaryTreeNode(5)
assert has_path_sum(tree, 8)
