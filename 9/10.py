from binary_tree_node import BinaryTreeNode

def find_successor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left

        return node

    while node.parent and node.parent.left is not node:
        node = node.parent

    return node.parent


#      3
#    2   5
root = BinaryTreeNode(3)
root.parent = None
assert not find_successor(root)
root.left = BinaryTreeNode(2)
root.left.parent = root
assert find_successor(root.left).data == 3
