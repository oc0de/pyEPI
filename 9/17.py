class BinaryTreeNode:
    def __init__(self):
        self.left = self.right = self.parent = None
        self._locked, self._num_locked_descendants = False, 0

    def is_locked(self):
        return self._locked

    def lock(self):
        if self._locked or self._num_locked_descendants > 0: return False

        curr = self.parent
        while curr:
            if curr._locked > 0: return False
            curr = curr.parent

        self._locked = True
        curr = self.parent
        while curr:
            curr._num_locked_descendants += 1
            curr = curr.parent
        return True

    def unlock(self):
        if self._locked:
            self._locked = False
            curr = self.parent
            while curr:
                curr._num_locked_descendants -= 1
                curr = curr.parent

root = BinaryTreeNode()
root.left = BinaryTreeNode()
root.left.parent = root
root.right = BinaryTreeNode()
root.right.parent = root
root.left.left = BinaryTreeNode()
root.left.left.parent = root.left
root.left.right = BinaryTreeNode()
root.left.right.parent = root.left

assert not root.is_locked()
assert root.lock()
# Should output True.
assert root.is_locked()
assert not root.left.lock()
root.unlock()
assert root.left.lock()
assert not root.lock()
assert root.left.is_locked()
