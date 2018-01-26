from ListNode import ListNode
overlap = __import__('4')

def overlapping_no_cycle_lists(l1,l2):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    l1_len, l2_len = length(l1), length(l2)
    if l1_len < l2_len: #l1 always is the longer list
        l1, l2 = l2, l1

    for _ in range(abs(l1_len - l2_len)):
        l1 = l1.next

    while l1 and l2 and l1 is not l2:
        l1, l2 = l1.next, l2.next

    return l1

L1 = ListNode(1, ListNode(2, ListNode(3, None)))
L2 = L1.next.next
assert overlapping_no_cycle_lists(L1, L2).data == 3
