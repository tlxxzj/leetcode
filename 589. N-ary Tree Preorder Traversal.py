"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        q = []
        if root:
            q = [root]
        while len(q) > 0:
            node = q.pop()
            res.append(node.val)
            if node.children:
                q.extend(list(node.children)[::-1])
        return res
            
