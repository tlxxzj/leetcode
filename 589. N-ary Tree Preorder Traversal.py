"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def pre(arr, r):
            if r:
                arr.append(r.val)
                if r.children:
                    for child in r.children:
                        pre(arr, child)
        
        ret = []
        pre(ret, root)
        return ret