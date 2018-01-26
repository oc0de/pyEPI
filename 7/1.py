from ListNode import ListNode

def merge_two_sorted_lists(l1,l2):
    dummy_head = tail = ListNode()
    while l1 and l2:
        if l1.data > l2.data:
            tail.next, l2 = l2, l2.next
        else:
            tail.next, l1 = l1, l1.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy_head.next

l1 = ListNode(12)
l2 = None
res = merge_two_sorted_lists(l1,l2)
assert res.data == 12 and res.next == None
