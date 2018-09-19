# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse_list(h):
            if h is None or h.next is None:
                return h
            p = None
            while h:
                h2 = h.next
                h.next = p
                p = h
                h = h2
            return p
            
        
        if head is None:
            return True
        
        if head.next is None:
            return True
        
        mid, h = head, head
        mp = None
        while h and h.next:
            mp = mid
            mid = mid.next
            h = h.next.next
        
        if h is None and mp:
            mp.next = None
        h1 = head
        h2 = reverse_list(mid)
        print(h1.val, h2.val)
        while h1:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        return True
        
        