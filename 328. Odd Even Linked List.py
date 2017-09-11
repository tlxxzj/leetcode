# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next) or (not head.next.next):
            return head
        
        def iterlist(h):
            while h:
                x = h.next
                yield h
                h = x
        
        tail1, tail2, h2 = head, head.next, head.next
        i = 0
        for h in iterlist(head.next.next):
            print h.val
            i += 1
            if i&1:
                tail1.next = h
                tail1 = h
            else:
                tail2.next = h
                tail2 = h
        tail1.next = h2
        tail2.next = None
        
        return head
            
        
        
        