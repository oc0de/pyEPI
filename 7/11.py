from ListNode import ListNode

def is_linked_list_palindrome(L):
    def reversed_list(head):
        curr, prev = head, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    if not L: return True
    slow = fast = L

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    slow, reversed_second_part = L, reversed_list(slow)

    while slow and reversed_second_part:
        if slow.data != reversed_second_part.data: return False
        slow, reversed_second_part = slow.next, reversed_second_part.next


    return True

L = ListNode(2, ListNode(3, ListNode(5, ListNode(3, ListNode(2, None)))))
assert is_linked_list_palindrome(L) == True

L = ListNode(2, ListNode(3, ListNode(3, ListNode(2, None))))
assert is_linked_list_palindrome(L) == True

L = ListNode(1, ListNode(2, ListNode(3, None)))
assert is_linked_list_palindrome(L) == False
