from ListNode import ListNode

def merge_two_sorted_doubly_lists(L1, L2):
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1.data > L2.data:
            tail.next = L2
            L2 = L2.next
        else:
            tail.next = L1
            L1 = L1.next

        tmp = tail
        tail = tail.next
        tail.prev = tmp

    tail.next = L1 or L2
    if tail.next:
        tail.next.prev = tail

    return dummy_head.next

l1 = ListNode(1)
l2 = None
res = merge_two_sorted_doubly_lists(l1,l2)
print res.data
