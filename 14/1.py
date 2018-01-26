from BST import BinaryTreeNode

def is_binary_tree_bst(tree, low_range=float('-inf'), hight_range=float('inf')):
    if not tree: return True
    if not low_range <= tree.data <= hight_range: return False
    return (is_binary_tree_bst(tree.left, low_range, tree.data) and
                is_binary_tree_bst(tree.right, tree.data, hight_range))


#      3
#    2   5
#  1    4 6
tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)
# should output True.
assert is_binary_tree_bst(tree)

tree.data = 10
# should output False.
assert not is_binary_tree_bst(tree)
