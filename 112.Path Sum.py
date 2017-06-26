# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def has(root, sum):
            sum -= root.val
            if root.left is None and root.right is None:
                return sum  == 0
            if root.left and has(root.left, sum):
                return True
            if root.right and has(root.right, sum):
                return True
            return False
        if root is None:
            return False
        else:
            return has(root, sum)