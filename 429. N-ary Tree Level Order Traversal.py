"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ret = []
        q = [root] if root else []
        while len(q) > 0:
            ret.append([node.val for node in q])
            q2 = []
            for node in q:
                if node.children:
                    for n in node.children:
                        q2.append(n)
            q = q2
        return ret