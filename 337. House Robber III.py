# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        d1 = {}
        d2 = {}
        def dp(node, rob_parent):
            if not node:
                return 0
            if rob_parent:
                if node in d1:
                    return d1[node]
                a = dp(node.left, False) + dp(node.right, False)
                d1[node] = a
                return a
            else:
                if node in d1:
                    a = d1[node]
                else:
                    a = dp(node.left, False) + dp(node.right, False)
                if node in d2:
                    b = d2[node]
                else:
                    b = node.val + dp(node.left, True) + dp(node.right, True)
                return max(a, b)
        return dp(root, False)