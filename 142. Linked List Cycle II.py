# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h1, h2 = head, head
        while h1 and h2:
            h1 = h1.next
            h2 = h2.next
            if h2:
                h2 = h2.next
            if h1 and h1 == h2:
                h2 = head
                while h1 != h2:
                    h1 = h1.next
                    h2 = h2.next
                return h1
        return None