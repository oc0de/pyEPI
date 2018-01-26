class BinaryTreeNode:

    def __init__(self, data=None, left=None, right=None, nxt=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = nxt  # Populates this field.


def construct_right_sibling(tree):
    def populate_children_next_field(subtree):
        while subtree and subtree.left:
            subtree.left.next = subtree.right
            subtree.right.next = subtree.next and subtree.next.left
            subtree = subtree.next

    while tree and tree.left:
        populate_children_next_field(tree)
        tree = tree.left

#      3
#    2   5
#  1  7 4 6
root = BinaryTreeNode(3)
root.left = BinaryTreeNode(2)
root.left.right = BinaryTreeNode(7)
root.left.left = BinaryTreeNode(1)
root.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(4)
root.right.right = BinaryTreeNode(6)
construct_right_sibling(root)
assert root.next is None
assert root.left.next is root.right
assert root.left.left.next is root.left.right
assert root.left.right.next is root.right.left
assert root.right.left.next is root.right.right
