from ListNode import ListNode

def even_odd_merge_original(L):
    if not L: return L

    even_head = even_tail = ListNode(0, None)
    odd_head = odd_tail = ListNode(0, None)
    curr = L

    while curr:
        if curr.data % 2 == 0:
            even_tail.next = curr
            even_tail = curr
        else:
            odd_tail.next = curr
            odd_tail = curr

        curr = curr.next

    even_tail.next = odd_head
    odd_tail.next = None

    return even_head.next

L = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
res = even_odd_merge_original(L)
while res:
    print res.data
    res = res.next
