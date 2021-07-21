# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b, c, d= headA, headB, headA, headB
        while a and b:
            a, b = a.next, b.next
        while a:
            a, c = a.next, c.next
        while b:
            b, d = b.next, d.next
        while c and d:
            if c == d:
                return c
            c, d = c.next, d.next
        return None
        