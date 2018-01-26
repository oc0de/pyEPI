from BST import BinaryTreeNode

def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0,
                                                possible_anc_or_desc_1, middle):
    search_0, search_1 = possible_anc_or_desc_0, possible_anc_or_desc_1
    while (search_0 is not possible_anc_or_desc_1 and search_0 is not middle and
            search_1 is not possible_anc_or_desc_0 and search_1 is not middle and
            (search_0 or search_1)):

        if search_0:
            search_0 = (search_0.left if middle.data < search_0.data
                        else search_0.right)

        if search_1:
            search_1 = (search_1.left if middle.data < search_1.data
                        else search_1.right)

    if ((search_0 is not middle and search_1 is not middle) or
        search_0 is possible_anc_or_desc_1 or
        search_1 is possible_anc_or_desc_0): return False

    def search_target(source, target):
        while source and source is not target:
            source = source.left if source.data > target.data else source.right
        return source is target

    return search_target(middle,
        possible_anc_or_desc_1 if search_0 is middle
        else possible_anc_or_desc_0)


    root = BinaryTreeNode(5)
    assert not pair_includes_ancestor_and_descendant_of_m(root, root, root)
    root.left = BinaryTreeNode(2)
    root.left.right = BinaryTreeNode(4)
    assert not pair_includes_ancestor_and_descendant_of_m(root, root.left,
                                                          root.left.right)
    assert pair_includes_ancestor_and_descendant_of_m(root, root.left.right,
                                                      root.left)

# Example of the first figure of BST chapter.
root = BinaryTreeNode(19)
root.left = BinaryTreeNode(7)
root.left.left = BinaryTreeNode(3)
root.left.left.left = BinaryTreeNode(2)
root.left.left.right = BinaryTreeNode(5)
root.left.right = BinaryTreeNode(11)
root.left.right.right = BinaryTreeNode(17)
root.left.right.right.left = BinaryTreeNode(13)
root.right = BinaryTreeNode(43)
root.right.left = BinaryTreeNode(23)
root.right.left.right = BinaryTreeNode(37)
root.right.left.right.left = BinaryTreeNode(29)
root.right.left.right.left.right = BinaryTreeNode(31)
root.right.left.right.right = BinaryTreeNode(41)
root.right.right = BinaryTreeNode(47)
root.right.right.right = BinaryTreeNode(53)
assert not pair_includes_ancestor_and_descendant_of_m(root.right, root.left,
                                                      root.right.left)
assert pair_includes_ancestor_and_descendant_of_m(
    root, root.right.left.right.left.right, root.right.left)
