from binary_tree_node import BinaryTreeNode

def get_inorder(tree):
    s, result = [], []
    while s or tree:
        if tree:
            s += tree,
            tree = tree.left
        else:
            tree = s.pop()
            result += tree.data,
            tree = tree.right

    return result

#        43
#    23     47
#      37      53
#    29  41
#     31
tree = BinaryTreeNode(43)
tree.left = BinaryTreeNode(23)
tree.left.right = BinaryTreeNode(37)
tree.left.right.left = BinaryTreeNode(29)
tree.left.right.left.right = BinaryTreeNode(31)
tree.left.right.right = BinaryTreeNode(41)
tree.right = BinaryTreeNode(47)
tree.right.right = BinaryTreeNode(53)
result = get_inorder(tree)
print result
assert get_inorder(tree) == [23, 29, 31, 37, 41, 43, 47, 53]
