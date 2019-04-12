# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ret = []
        h = head
        q = []
        while h:
            while len(q) > 0 and h.val > q[-1].val:
                q[-1].nexti = h.val
                q.pop()
            h.nexti = 0
            q.append(h)
            h = h.next
        
        h = head
        while h:
            ret.append(h.nexti)
            h = h.next
        return ret