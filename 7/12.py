from ListNode import ListNode

def list_pivoting(L, key):
    if not L: return L

    curr = L
    less_head = less_tail = ListNode()
    equal_head = equal_tail = ListNode()
    greater_head = greater_tail = ListNode()

    while curr:
        if curr.data < key:
            less_tail.next = curr
            less_tail = curr
        elif curr.data == key:
            equal_tail.next = curr
            equal_tail = curr
        else:
            greater_tail.next = curr
            greater_tail = curr

        curr = curr.next

    greater_tail.next = None
    less_tail.next = equal_head.next
    equal_tail.next = greater_head.next

    return less_head.next

L = ListNode(6, ListNode(7, ListNode(3, ListNode(4, ListNode(5, ListNode(1, ListNode(2)))))))
res = list_pivoting(L, 3)
while res:
    print res.data
    res = res.next
