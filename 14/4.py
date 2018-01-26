from BST import BinaryTreeNode

def find_LCA(tree, n1, n2):
    if not tree: return None

    if tree.data > n1.data and tree.data > n2.data: return find_LCA(tree.left, n1, n2)
    if tree.data < n1.data and tree.data < n2.data: return find_LCA(tree.right, n1, n2)
    return tree


#      3
#    2   5
#  1    4 6
tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)
assert 3 == find_LCA(tree, tree.left.left, tree.right.left).data
assert 5 == find_LCA(tree, tree.right.left, tree.right.right).data
assert 2 == find_LCA(tree, tree.left.left, tree.left).data
