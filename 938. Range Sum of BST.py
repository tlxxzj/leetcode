# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        result = 0
        if not root:
            return result
        if L <= root.val <= R:
            result += root.val
        return result + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        