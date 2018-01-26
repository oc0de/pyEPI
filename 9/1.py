from binary_tree_node import BinaryTreeNode

def is_balanced_binary_tree(tree):
    def helper(tree):
        if not tree: return 0
        left_side = helper(tree.left)
        if left_side == -1: return -1
        right_side = helper(tree.right)
        if right_side == -1: return -1
        if abs(left_side - right_side) > 1: return -1

        return max(left_side, right_side) + 1

    return True if helper(tree) != -1 else False


#  balanced binary tree test
#      3
#    2   5
#  1    4 6

root = BinaryTreeNode(3)
root.left = BinaryTreeNode(2)
root.left.left = BinaryTreeNode(1)
# root.left.left.left = BinaryTreeNode(1)
root.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(4)
root.right.right = BinaryTreeNode(6)

assert is_balanced_binary_tree(root) == True
