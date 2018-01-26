from ListNode import ListNode
cycle = __import__('3')
overlap = __import__('4')

def overlapping_lists(L1, L2):
    def get_distance(s, f):
        distance = 0
        while s is not f:
            s = s.next
            distance += 1

        return distance

    root1, root2 = cycle.has_cycle(L1), cycle.has_cycle(L2)
    if not root1 and not root2:
        return overlap.overlapping_lists(L1, L2)

    if (root1 and not root2) or (not root1 and root2):
        return None

    temp = root1
    while True:
        if (temp is root1) or (temp is root2): break

    if temp is not root2: return None
    l1_length, l2_length = get_distance(L1, root1), get_distance(L2, root2)

    if l1_length < l2_length:
        root1, root2 = root2, root1
        L1, L2 = L2, L1

    for _ in range(l1_length - l2_length):
        L1 = L1.next

    while L1 is not L2 and L1 is not root1 and L2 is not root2:
        L1, L2 = L1.next, L2.next

    return L1 if L1 is L2 else root1


# L1: 1->2->3->4->5->6-
#              ^  ^    |
#              |  |____|
# L2: 7->8-----
L1 = ListNode(1,
              ListNode(2,
                       ListNode(3,
                                ListNode(4, ListNode(5, ListNode(6,
                                                                 None))))))
L1.next.next.next.next.next.next = L1.next.next.next.next

L2 = ListNode(7, ListNode(8, None))
L2.next.next = L1.next.next.next
assert overlapping_lists(L1, L2).data == 4

# L1: 1->2->3->4->5->6-
#           ^     ^    |
#           |     |____|
# L2: 7->8---
L2.next.next = L1.next.next
assert overlapping_lists(L1, L2).data == 3
