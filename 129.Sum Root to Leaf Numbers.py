# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumTree(root, n):
            if root is None: return 0
            if root.left is None and root.right is None: return n*10+root.val
            return sumTree(root.left, n*10+root.val) + sumTree(root.right, n*10+root.val)
        return sumTree(root, 0)