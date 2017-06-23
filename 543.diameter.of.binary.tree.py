# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        self._getH(root)
        return self.diameter
    
    def _getH(self, node):
        if node is None: return 0
        lh = self._getH(node.left)
        rh = self._getH(node.right)
        self.diameter = max(self.diameter, lh+rh)
        return max(lh, rh) + 1