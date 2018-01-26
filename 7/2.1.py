from ListNode import ListNode

def reverse_linked_list(L):
    head, prev = L, None
    while head:
        tmp, head.next = head.next, prev
        prev, head = head, tmp
    return prev

L = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, None)))))))
res = reverse_linked_list(L)
