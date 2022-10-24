# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m, n = 0, 0
        taila, tailb = None, None
        h = headA
        while h:
            taila = h
            m += 1
            h = h.next
        h = headB
        while h:
            tailb = h
            n += 1
            h = h.next
        if taila != tailb:
            return None
        if m > n:
            for i in range(m-n):
                headA = headA.next
        else:
            for i in range(n - m):
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
        