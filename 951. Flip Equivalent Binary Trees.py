# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getVal(node):
            if node:
                return node.val
            return None   
        if getVal(root1) != getVal(root2):
            return False
        if not root1:
            return True
        l1, r1, l2, r2 = root1.left, root1.right, root2.left, root2.right
        return (self.flipEquiv(l1, l2) and self.flipEquiv(r1, r2)) or(self.flipEquiv(l1, r2) and self.flipEquiv(r1, l2))