# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        s1 = []
        s2 = []
        if root: s1.append(root)
        while len(s1) > 0:
            ret.append([])
            for node in s1:
                ret[-1].append(node.val)
                if node.left: s2.append(node.left)
                if node.right: s2.append(node.right)
            s1, s2 = s2, []
        return ret[::-1]