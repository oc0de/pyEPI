from BST import BinaryTreeNode
import collections

Interval = collections.namedtuple('Interval', ('left', 'right'))

def range_lookup_in_bst(tree, interval):
    def helper(tree):
        if not tree: return None

        if interval.left <= tree.data <= interval.right:
            helper(tree.left)
            result.append(tree.data)
            helper(tree.right)

        elif tree.data < interval.left:
            helper(tree.right)

        else:
            helper(tree.left)

    result = []
    helper(tree)
    return result


def main():
    #          19
    #     7          43
    #   3   11   23     47
    # 2  5    17   37      53
    #        13  29  41
    #             31
    tree = BinaryTreeNode(19)
    tree.left = BinaryTreeNode(7)
    tree.left.left = BinaryTreeNode(3)
    tree.left.left.left = BinaryTreeNode(2)
    tree.left.left.right = BinaryTreeNode(5)
    tree.left.right = BinaryTreeNode(11)
    tree.left.right.right = BinaryTreeNode(17)
    tree.left.right.right.left = BinaryTreeNode(13)
    tree.right = BinaryTreeNode(43)
    tree.right.left = BinaryTreeNode(23)
    tree.right.left.right = BinaryTreeNode(37)
    tree.right.left.right.left = BinaryTreeNode(29)
    tree.right.left.right.left.right = BinaryTreeNode(31)
    tree.right.left.right.right = BinaryTreeNode(41)
    tree.right.right = BinaryTreeNode(47)
    tree.right.right.right = BinaryTreeNode(53)
    assert sorted(
        range_lookup_in_bst(tree, Interval(16, 31))) == [17, 19, 23, 29, 31]
    assert len(range_lookup_in_bst(tree, Interval(38, 39))) == 0
    assert range_lookup_in_bst(tree, Interval(38, 42)) == [41]
    assert len(range_lookup_in_bst(tree, Interval(-1, 1))) == 0
    

if __name__ == '__main__':
    main()
