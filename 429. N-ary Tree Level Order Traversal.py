"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        q = [root]
        while len(q) > 0:
            q2 = []
            x = []
            for r in q:
                x.append(r.val)
                if r.children:
                    for c in r.children:
                        q2.append(c)
            q = q2
            ret.append(x)
        return ret
        