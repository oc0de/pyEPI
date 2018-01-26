from binary_tree_node import BinaryTreeNode

def inorder_traversal(tree):
    curr, prev, next_node, result = tree, None, None, []
    while curr:
        if curr.parent is prev:
            if curr.left:
                next_node = curr.left
            else:
                result += curr.data,
                next_node = curr.right or curr.parent
        elif curr.left is prev:
            result += curr.data,
            next_node = curr.right or curr.parent
        else:
            next_node = curr.parent

        prev, curr = curr, next_node

    return result

#      3
#    2   5
#  1    4 6
root = BinaryTreeNode(3)
root.parent = None
assert inorder_traversal(root) == [3]
root.left = BinaryTreeNode(2)
root.left.parent = root
root.left.left = BinaryTreeNode(1)
root.left.left.parent = root.left
assert inorder_traversal(root) == [1, 2, 3]

root.right = BinaryTreeNode(5)
root.right.parent = root
root.right.left = BinaryTreeNode(4)
root.right.left.parent = root.right
root.right.right = BinaryTreeNode(6)
root.right.right.parent = root.right

assert inorder_traversal(root) == [1, 2, 3, 4, 5, 6]
