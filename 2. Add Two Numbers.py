# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        l3_head = l3
        l0_value = 0
        while l1 or l2:
            l1_value, l2_value = 0, 0
            if l1:
                l1_value = l1.val
                l1 = l1.next
            if l2:
                l2_value = l2.val
                l2 = l2.next
            l3_value = (l0_value + l1_value + l2_value) % 10
            l0_value = (l0_value + l1_value + l2_value) // 10
            l3.next = ListNode(l3_value)
            l3 = l3.next
        if l0_value > 0:
            l3.next = ListNode(l0_value)
        return l3_head.next