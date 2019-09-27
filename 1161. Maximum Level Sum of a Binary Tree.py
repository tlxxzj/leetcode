# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = []
        q = [root]
        q2 = []
        while len(q) > 0:
            s = 0
            q2 = []
            for node in q:
                s += node.val
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            level.append(s)
            q = q2
        return level.index(max(level)) + 1
