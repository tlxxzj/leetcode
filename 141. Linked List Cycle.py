# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a, b = None, None
        if head:
            a = head
            if head.next:
                b = a.next
        while a and b:
            if a == b:
                return True
            a = a.next
            if b.next:
                b = b.next.next
            else:
                return False
        return False