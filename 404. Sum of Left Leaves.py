# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = 0
        if root.left:
            node = root.left
            if node.left is None and node.right is None:
                left = node.val
            else:
                left = self.sumOfLeftLeaves(root.left)
        return left + self.sumOfLeftLeaves(root.right)
