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
        while l1_ptr or l2_ptr:
            if l1_ptr and l2_ptr:
                carry, digit = divmod(l1_ptr.val + l2_ptr.val + carry, 10)
            elif l1_ptr:
                carry, digit = divmod(l1_ptr.val + carry, 10)
            elif l2_ptr:
                carry, digit = divmod(l2_ptr.val + carry, 10)
            new_node = ListNode(val=digit, next=None)
            result_ptr.next = new_node

            result_ptr = new_node
            if l1_ptr:
                l1_ptr = l1_ptr.next
            if l2_ptr:
                l2_ptr = l2_ptr.next
        if carry > 0:  # when carry happens at MSB
            last_node = ListNode(val=carry, next=None)
            result_ptr.next = last_node
        return dummy.next