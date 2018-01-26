from binary_tree_node import BinaryTreeNode

def find_kth_node_binary_tree(tree, k):
    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < k:
            tree = tree.right
            k -= left_size + 1
        elif left_size + 1 == k: return tree
        else:
            tree = tree.left

    return None

#  size field
#      6
#    2   3
#  1    1 1
#
#  data field
#      3
#    2   5
#  1    4 6
root = BinaryTreeNode()
root.size = 6
root.data = 3
root.left = BinaryTreeNode()
root.left.size = 2
root.left.data = 2
root.left.left = BinaryTreeNode()
root.left.left.size = 1
root.left.left.data = 1
root.right = BinaryTreeNode()
root.right.size = 3
root.right.data = 5
root.right.left = BinaryTreeNode()
root.right.left.size = 1
root.right.left.data = 4
root.right.right = BinaryTreeNode()
root.right.right.size = 1
root.right.right.data = 6

assert find_kth_node_binary_tree(root, 3).data == 3
assert find_kth_node_binary_tree(root, 4).data == 4
assert find_kth_node_binary_tree(root, 6).data == 6
