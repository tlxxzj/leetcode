# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        def gen(l, r):
            nodes = []
            if l > r:
                return [None]
            for m in range(l, r+1):
                lnodes = gen(l, m-1)
                rnodes = gen(m+1, r)
                for ln in lnodes:
                    for rn in rnodes:
                        root = TreeNode(m)
                        root.left = ln
                        root.right = rn
                        nodes.append(root)
            return nodes

        return gen(1, n)