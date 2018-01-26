from binary_tree_node import BinaryTreeNode

def preorder_traversal(tree):
    path, result = [tree], []
    while path:
        curr = path.pop()
        if curr:
            result += curr.data,
            path += [curr.right, curr.left]

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
res = preorder_traversal(tree)
assert res == [3,2,1,5,4,6]
