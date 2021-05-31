# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def sum(root, val):
            if not root:
                return 0
            val = val * 10 + root.val
            if (not root.left) and (not root.right):
                return val
            return sum(root.left, val) + sum(root.right, val)
        
        return sum(root, 0)