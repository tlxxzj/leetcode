# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k<=1 or not head:
            return head
        
        def walk(h):
            while h:
                x=h.next
                yield h
                h=x
        
        def reverse(h):
            t=None
            for x in walk(h):
                x.next=t
                t=x
            return t
        
        def add(h, t, v):
            if not h:
                h=t=v
            else:
                t.next=v
                t=v
            return [h, t]
        
        def printlist(h):
            for x in walk(h):
                print x.val, 
            print ''
        
        c=1
        h = t = head
        head = tail = None
        while t:
            if c % k == 0:
                x = t.next
                t.next = None
                #printlist( reverse(h) )
                head, tail = add(head, tail, reverse(h))
                #printlist( head )
                tail = h
                h = x
                t = x
                c += 1
            else:
                t = t.next
                c += 1
        if h:
            head, tail = add(head, tail, h)
        
        return head
        
        
            
        