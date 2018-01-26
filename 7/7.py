from ListNode import ListNode

def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next
    second.next = second.next.next
    return dummy_head.next

L = ListNode(1, ListNode(2, ListNode(3, None)))
L = remove_kth_last(L, 2)

assert L.data == 1 and L.next.data == 3
L = remove_kth_last(L, 2)
assert L.data == 3 and L.next is None
# L = remove_kth_last(L, 1)
# assert not L
