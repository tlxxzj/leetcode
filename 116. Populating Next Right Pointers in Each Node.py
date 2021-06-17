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
        q = []
        if root:
            q.append(root)
        
        while len(q) > 0:
            q2 = []
            previous_node = None
            for node in q:
                if previous_node:
                    previous_node.next = node
                previous_node = node
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q = q2

        return root