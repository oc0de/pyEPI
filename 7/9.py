from ListNode import ListNode

def cyclically_right_shift_list(L, k):
    if not L: return L
    tail, n = L, 1
    while tail.next:
        n += 1
        tail = tail.next

    k %= n
    if k == 0: return L
    steps, tail.next = n-k, L

    while steps > 0:
        steps -= 1
        tail = tail.next

    new_head = tail.next
    tail.next = None

    return new_head

L = ListNode(1)
assert cyclically_right_shift_list(L, 2) is L
L = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
assert cyclically_right_shift_list(L, 2).data is 4
