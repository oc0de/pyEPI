from binary_tree_node import BinaryTreeNode

def is_symmetric(tree):
    def helper(t1, t2):
        if not t1 and not t2: return True
        elif t1 and t2:
            return t1.data == t2.data and helper(t1.left, t2.right) and helper(t1.right, t2.left)
        return False

    return not tree or helper(tree.left, tree.right)

tree = BinaryTreeNode()
assert is_symmetric(tree)

tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(2)
assert is_symmetric(tree)

tree.left.right = BinaryTreeNode(3)
tree.right.left = BinaryTreeNode(3)
assert is_symmetric(tree)
