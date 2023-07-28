# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def find(node):
            if not node:
                return 0, 0
            ls, lt = find(node.left)
            rs, rt = find(node.right)
            return node.val + ls + rs, abs(ls-rs) + lt + rt
        
        s, t = find(root)
        return t