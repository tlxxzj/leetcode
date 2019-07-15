# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def visit(ro, val):
            if ro is None:
                return val
            val = visit(ro.right, val)
            ro.val += val
            return visit(ro.left, ro.val)
        
        visit(root, 0)
        return root