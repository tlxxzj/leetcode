# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        s1, s2 = [], []
        if root: s1 = [root]
        while len(s1):
            ret.append(s1[-1].val)
            for node in s1:
                if node.left: s2.append(node.left)
                if node.right: s2.append(node.right)
            s1, s2 = s2, []
        return ret