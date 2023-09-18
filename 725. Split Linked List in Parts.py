# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if k == 1:
            return [head]
        
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        
        x, y = n // k, n % k
        res = []
        node = head
        for i in range(k):
            res.append(node)
            z = x
            if i < y:
                z += 1
            for j in range(1, z):
                if node:
                    node = node.next
            
            if node:
                nextNode = node.next
                node.next = None
                node = nextNode
        
        return res
