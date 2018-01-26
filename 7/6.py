from ListNode import ListNode

def deletion_from_list(node_to_delete):
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next

L = ListNode(1, ListNode(2, ListNode(3, None)))
deletion_from_list(L)
assert L.data == 2 and L.next.data == 3
