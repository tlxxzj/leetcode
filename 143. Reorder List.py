# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if (not head) or (not head.next) or (not head.next.next):
            return
            
        def walk(h):
            while h:
                n = h.next
                yield h
                h = n
        
        def reverse(h):
            r = None
            for x in walk(h):
                x.next = r
                r=x
            return r
        
        def walk2(h1, h2):
            g1 = walk(h1)
            g2 = walk(h2)
            while True:
                yield g1.next()
                yield g2.next()
            
        
        h, h2 = head, head.next.next
        while h2:
            h = h.next
            h2 = h2.next
            if h2:
                h2 = h2.next
        a = head.next
        b = h.next
        h.next = None
        b = reverse(b)
        
        tail = head
        for n in walk2(b, a):
            tail.next = n
            tail = n

        