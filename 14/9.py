from BST import BinaryTreeNode

def build_min_height_bst_from_sorted_array(A):
    def helper(start, end):
        if start >= end: return None
        mid = (start + end) / 2
        return BinaryTreeNode(A[mid], helper(start, mid), helper(mid+1, end))

    return helper(0, len(A))

A = [1, 2, 3, 4]
result = build_min_height_bst_from_sorted_array(A)
assert 3 == result.data
assert 2 == result.left.data
assert 1 == result.left.left.data
assert 4 == result.right.data
