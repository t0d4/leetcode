from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result_ptr = dummy
        l1_ptr = l1
        l2_ptr = l2
        carry = 0
        while l1_ptr or l2_ptr or (carry != 0):
            digit_sum = carry

            if l1_ptr:
                digit_sum += l1_ptr.val
                l1_ptr = l1_ptr.next
            if l2_ptr:
                digit_sum += l2_ptr.val
                l2_ptr = l2_ptr.next

            carry, digit = divmod(digit_sum, 10)

            new_node = ListNode(val=digit)
            result_ptr.next = new_node
            result_ptr = new_node
        return dummy.next
