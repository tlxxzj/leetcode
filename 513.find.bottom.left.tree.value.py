# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.h = 0
        self.val = None
        self._find(root, 1)
        return self.val
    
    def _find(self, root, h):
        if root is None: return
        if h > self.h:
            self.h = h
            self.val = root.val
        self._find(root.left, h+1)
        self._find(root.right, h+1)