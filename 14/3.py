from BST import BinaryTreeNode

def find_k_largest_in_bst(tree, k):
    def helper(tree):
        if tree and len(result) < k:
            helper(tree.right)
            if len(result) < k:
                result.append(tree.data)
                helper(tree.left)

    result = []
    helper(tree)
    return result

#      3
#    2   5
#  1    4 6
tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)

assert find_k_largest_in_bst(tree, 1) == [6]
assert find_k_largest_in_bst(tree, 2) == [6,5]
assert find_k_largest_in_bst(tree, 3) == [6,5,4]
