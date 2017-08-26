# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n: return head
        front, back = None, None
        k = 1
        h = head
        while k != m:
            front = h
            h = h.next
            k += 1
        #reverse
        p, q = h, h.next
        while k != n:
            x = q.next
            q.next = p
            p = q
            q = x
            k += 1
        if front:
            front.next = p
        else:
            head = p
        h.next = q
        return head


