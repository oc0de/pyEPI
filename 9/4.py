from binary_tree_node import BinaryTreeNode

def lca(n1, n2):
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    depth_n1, depth_n2 = get_depth(n1), get_depth(n2)
    if depth_n2 > depth_n1:
        n1, n2 = n2, n1

    depth_diff = abs(depth_n1 - depth_n2)
    while depth_diff > 0:
        n1 = n1.parent
        depth_diff -= 1

    while n1 is not n2:
        n1, n2 = n1.parent, n2.parent

    return n1

#      3
#    2   5
#  1    4 6
root = BinaryTreeNode(3, None, None, None)
root.left = BinaryTreeNode(2, None, None, root)
root.left.left = BinaryTreeNode(1, None, None, root.left)
root.right = BinaryTreeNode(5, None, None, root)
root.right.left = BinaryTreeNode(4, None, None, root.right)
root.right.right = BinaryTreeNode(6, None, None, root.right)

assert lca(root.left, root.right).data == 3
assert lca(root.right, root.right.right).data == 5
assert lca(root.right.left, root.right.right).data == 5
