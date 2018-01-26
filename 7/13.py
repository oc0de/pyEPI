from ListNode import ListNode

def add_two_numbers(num1, num2):
    head = dummy_head = ListNode()
    carry = 0
    while num1 or num2 or carry:
        val = (num1.data if num1 else 0) + (num2.data if num2 else 0) + carry
        num1 = num1.next if num1 else None
        num2 = num2.next if num2 else None
        dummy_head.next = ListNode(val % 10)
        carry, dummy_head = val // 10, dummy_head.next

    return head.next

L = ListNode(3, ListNode(4, ListNode(2)))
R = ListNode(7, ListNode(5, ListNode(7)))
S = add_two_numbers(L, R)
assert S.data == 0 and S.next.data == 0 and S.next.next.data == 0 and S.next.next.next.data == 1
