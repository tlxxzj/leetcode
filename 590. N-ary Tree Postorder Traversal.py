"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def post(arr, r):
            if r:
                if r.children:
                    for child in r.children:
                        post(arr, child)
                arr.append(r.val)
        
        ret = []
        post(ret, root)
        return ret