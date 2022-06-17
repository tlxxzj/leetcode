# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [(root, 1)]
        while len(q) > 0:
            q2 = []
            for node, d in q:
                if not node:
                    continue
                if (not node.left) and (not node.right):
                    return d
                q2.append((node.left, d+1))
                q2.append((node.right, d+1))
            q = q2