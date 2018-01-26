class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right


def binary_tree_depth_order(tree):
    if not tree: return []
    result, curr = [], [tree]

    while curr:
        result += [t.data for t in curr],
        parent, curr = curr, []
        for p in parent:
            if p.left: curr += p.left,
            if p.right: curr += p.right,

    return result

left = BinaryTreeNode(6, BinaryTreeNode(271), BinaryTreeNode(561))
right = BinaryTreeNode(6, BinaryTreeNode(2), BinaryTreeNode(271))
tree = BinaryTreeNode(314, left, right)
result = binary_tree_depth_order(tree)
print result
