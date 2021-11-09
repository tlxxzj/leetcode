"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = [root] if root else []
        while len(q) > 0:
            q2 = []
            for node in q:
                if node.left: q2.append(node.left)
                if node.right: q2.append(node.right)
            for i in range(len(q)-1):
                q[i].next = q[i+1]
            q = q2
        return root