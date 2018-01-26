from binary_tree_node import BinaryTreeNode
import collections

def lca(tree, n1, n2):
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    def lca_helper(tree, n1, n2):
        if not tree: return Status(0, None)
        left_result = lca_helper(tree.left, n1, n2)
        if left_result.num_target_nodes == 2: return left_result
        right_result = lca_helper(tree.right, n1, n2)
        if right_result.num_target_nodes == 2: return right_result
        num_target_nodes = (left_result.num_target_nodes + right_result.num_target_nodes + int(tree in (n1, n2)))

        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, n1, n2).ancestor

#      3
#    2   5
#  1    4 6
#   4
tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.left.left.right = BinaryTreeNode(4)
tree.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)
# should output 3
x = lca(tree, tree.left, tree.right)
assert x.data == 3

x = lca(tree, tree.left.left.right, tree.left.left)
assert x.data == 1

x = lca(tree, tree.right.left, tree.right.right)
assert x.data == 5
