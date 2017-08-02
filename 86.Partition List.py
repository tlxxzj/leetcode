# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        s1 = [ListNode(0)]
        s2 = [ListNode(0)]
        while head:
            if head.val < x:
                s1.append(head)
            else:
                s2.append(head)
            head = head.next
        
        for i in range(len(s1)-1):
            s1[i].next = s1[i+1]
        for i in range(len(s2)-1):
            s2[i].next = s2[i+1]
        s2[-1].next = None
        s1[-1].next = s2[0].next
 
        
        return s1[0].next
        