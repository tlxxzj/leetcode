# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        prev = head
        if head:
            node = head.next
            prev.next = None
        while node:
            node2 = node.next
            node.next = prev
            prev = node
            node = node2
        return prev
