# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self._convert(root, 0)
        return root
    
    def _convert(self, root, sum):
        if root is None: return 0
        val = root.val
        lsum = self._convert(root.right, sum)
        root.val += sum + lsum
        rsum = self._convert(root.left, root.val)
        return lsum + rsum + val