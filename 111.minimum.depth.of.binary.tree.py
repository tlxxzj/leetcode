# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.h = float('inf')
        self._min(root, 1)
        return self.h if self.h != float('inf') else 0
    
    def _min(self, root, h):
        if root is None: return
        if root.left is None and root.right is None:
            self.h = min(self.h, h)
        self._min(root.left, h+1)
        self._min(root.right, h+1)