from BST import BinaryTreeNode

def find_first_greater_than_k(tree, k):
    if not tree: return None

    subtree, result = tree, None
    while subtree:
        if subtree.data > k:
            result, subtree = subtree, subtree.left
        else:
            subtree = subtree.right

    return result


#      3
#    2   5
#  1    4 7
root = BinaryTreeNode(3)
root.left = BinaryTreeNode(2)
root.left.left = BinaryTreeNode(1)
root.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(4)
root.right.right = BinaryTreeNode(7)
assert find_first_greater_than_k(root, 1) is root.left
assert find_first_greater_than_k(root, 5) is root.right.right
assert find_first_greater_than_k(root, 6) is root.right.right
assert not find_first_greater_than_k(root, 7)
