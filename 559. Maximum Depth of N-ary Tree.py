"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        q = [root]
        while len(q) > 0:
            depth += 1
            q2 = []
            for r in q:
                if not r.children:
                    continue
                for child in r.children:
                    q2.append(child)
            q = q2
        return depth