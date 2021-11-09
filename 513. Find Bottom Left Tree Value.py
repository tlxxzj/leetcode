# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        ret = None
        q = [root] if root else []
        while len(q) > 0:
            q2 = []
            ret = q[0].val
            for node in q:
                if node.left: q2.append(node.left)
                if node.right: q2.append(node.right)
            q = q2
        return ret