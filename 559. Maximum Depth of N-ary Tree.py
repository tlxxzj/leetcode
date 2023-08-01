"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        q = []
        if root:
            q = [root]
        while len(q) > 0:
            depth += 1
            q2 = []
            for node in q:
                if node.children:
                    q2.extend(node.children)
            q = q2
        return depth
