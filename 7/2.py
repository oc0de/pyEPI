from ListNode import ListNode

def reverse_sublist(L, s, f):
    dummy_head = head = ListNode(0, L)
    for _ in range(1, s):
        head = head.next

    curr = head.next
    for _ in range(f-s):
        temp = curr.next
        curr.next = temp.next
        temp.next = head.next
        head.next = temp

    return dummy_head.next

L = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2,None)))))
result = reverse_sublist(L, 2, 4)
assert result.data == 11 and result.next.data == 7 and \
        result.next.next.data == 5 and result.next.next.next.data == 3 and \
         result.next.next.next.next.data == 2 and result.next.next.next.next.next is None
