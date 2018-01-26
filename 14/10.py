from BST import BinaryTreeNode

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def empty(self):
        return self._root is None

    def insert(self, key):
        if self.empty():
            self._root = BinaryTreeNode(key)

        else:
            parent = None
            curr = self._root

            while curr:
                parent = curr
                if key == curr: return False
                curr = curr.left if key < curr.data else curr.right

            if key < parent.data:
                parent.left = BinaryTreeNode(key)
            else:
                parent.right = BinaryTreeNode(key)

        return True

    def delete(self, key):
        curr = self._root
        parent = None

        while curr and curr.data != key:
            parent = curr
            curr = curr.left if key < curr.data else curr.right

        if not curr: return False

        key_node = curr
        if key_node.right:
            r_key_node = key_node.right
            r_parent = key_node

            while r_key_node.left:
                r_parent = r_key_node
                r_key_node = r_key_node.left

            key_node.data = r_key_node.data
            if r_parent.left == r_key_node:
                r_parent.left = r_key_node.right
            else:
                r_parent.right = r_key_node.right
        else:
            if self._root == key_node:
                self._root = key_node.left
            else:
                if parent.left == key_node:
                    parent.left = key_node.left
                else:
                    parent.right = key_node.left

        return True

    def get_root_val(self):
        return self._root.data


def main():
    bst = BinarySearchTree()
    assert bst.empty() is True
    assert bst.insert(7) is True
    assert bst.insert(8) is True
    assert bst.insert(9) is True
    assert bst.insert(4) is True
    assert bst.insert(3) is True
    assert bst.empty() is False
    assert bst.insert(2) is True
    assert bst.insert(5) is True
    assert bst.delete(7) is True
    assert bst.delete(9) is True
    # should output 8
    assert bst.get_root_val() == 8
    assert bst.delete(4) is True
    # should output 8
    assert bst.get_root_val() == 8
    assert bst.delete(8) is True
    # should output 5
    assert bst.get_root_val() == 5
    assert bst.delete(5) is True
    assert bst.delete(3) is True
    # should output 2
    assert bst.get_root_val() == 2
    assert bst.delete(2) is True
    assert bst.delete(1) is False
    assert bst.empty() is True
    bst.insert(7)
    assert bst.get_root_val() == 7
    bst.insert(9)
    assert bst.get_root_val() == 7
    bst.delete(7)
    assert bst.get_root_val() == 9


if __name__ == '__main__':
    main()
