from ListNode import ListNode

def has_cycle(head):
    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None


L3 = ListNode(3, None)
L2 = ListNode(2, L3)
L1 = ListNode(1, L2)

assert has_cycle(L1) is None

L3.next = L2
assert has_cycle(L1).data == 2
