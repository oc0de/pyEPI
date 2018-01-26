from ListNode import ListNode

def remove_duplicates(L):
    curr_node = L
    while curr_node:

        next_node = curr_node.next
        while next_node and next_node.data == curr_node.data:
            next_node = next_node.next

        curr_node.next = next_node
        curr_node = next_node


L = ListNode(1, ListNode(1, ListNode(3, ListNode(3, ListNode(5, None)))))
remove_duplicates(L)

assert L.data == 1 and L.next.data == 3 and L.next.next.data == 5
