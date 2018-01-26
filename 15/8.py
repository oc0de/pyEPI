from binary_tree_node import BinaryTreeNode

def generate_all_binary_trees(num_nodes):
    if num_nodes == 0: return [None]

    result = []
    for num_left_nodes in range(num_nodes):
        left_subtrees = generate_all_binary_trees(num_left_nodes)
        right_subtrees = generate_all_binary_trees(num_nodes - num_left_nodes - 1)
        result += [BinaryTreeNode(0, left, right)
                    for left in left_subtrees
                    for right in right_subtrees
        ]
    print result
    return result

assert len(generate_all_binary_trees(3)) == 5
