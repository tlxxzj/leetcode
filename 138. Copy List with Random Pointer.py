"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        root = Node(0)
        r = root
        h = head
        newNodes = {}
        while h:
            r.next = Node(h.val)
            newNodes[h] = r.next
            r = r.next
            h = h.next
        
        r = root.next
        h = head
        while h:
            if h.random:
                r.random = newNodes[h.random]
            h = h.next
            r = r.next
        return root.next