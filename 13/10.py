class ListNode:
    def __init__(self, data = 0, next_node = None, prev_node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


def stable_sort_list(L):
    if not L and not L.next: return L
    pre_slow, slow, fast = None, L, L

    while fast and fast.next:
        pre_slow = slow
        slow = slow.next
        fast = fast.next.next

    pre_slow.next = None
    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))
