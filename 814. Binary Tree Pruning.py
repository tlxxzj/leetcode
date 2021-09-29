# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(node):
            if not node:
                return 0
            l, r = prune(node.left), prune(node.right)
            if l == 0:
                node.left = None
            if r == 0:
                node.right = None
            return node.val | l | r
        
        if (not root) or ((root.val | prune(root)) == 0):
            return None
        return root
        