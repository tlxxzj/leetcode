# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        def getl(h):
            l = 0
            while h:
                l += 1
                h = h.next
            return l
        if head is None or k <=0:
            return head
        L = getl(head)
        k = k%L
        if k == 0 or L <= 1:
            return head
        x = L - k - 1
        h = head
        while x > 0:
            x -= 1
            h = h.next
        ret = h.next
        h.next = None
        h = ret
        while h.next:
            h = h.next
        h.next = head
        return ret
        
        
        
        