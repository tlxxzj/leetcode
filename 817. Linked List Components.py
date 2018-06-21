# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)
        cnt = 0
        while head:
            if head.val in G:
                cnt += 1
                while head.next and head.next.val in G:
                    head = head.next
            head = head.next
        return cnt