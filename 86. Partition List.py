# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        r1, r2 = ListNode(), ListNode()
        h1, h2 = r1, r2
        while head:
            if head.val < x:
                h1.next = head
                h1 = h1.next
            else:
                h2.next = head
                h2 = h2.next
            head = head.next
        h1.next = r2.next
        h2.next = None
        return r1.next
