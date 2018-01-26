from binary_tree_node import BinaryTreeNode

def find_all_path(tree, remaining_weight):
    result = []
    def find_all_path(tree, remaining_weight, partial_path, result):
        if not tree:
            return None
        if not tree.left and not tree.right and remaining_weight == tree.data:
            result += partial_path + [tree.data],
            return

        find_all_path(tree.left, remaining_weight - tree.data, partial_path + [tree.data], result)
        find_all_path(tree.right, remaining_weight - tree.data, partial_path + [tree.data], result)

    find_all_path(tree, remaining_weight, [], result)
    return result


#      3
#    2   5
#  7    4 6

tree = BinaryTreeNode(3)
res = find_all_path(tree, 10)
assert res == []
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(5)
tree.left.left = BinaryTreeNode(7)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)
res = find_all_path(tree, 12)
print res
