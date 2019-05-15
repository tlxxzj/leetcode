# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ret = 0
        q = [[root, root.val, root.val]]
        while len(q) > 0:
            node, val1, val2 = q.pop()
            ret = max(ret, abs(val1 - node.val), abs(val2 - node.val))
            val1, val2 = max(val1, node.val), min(val2, node.val)
            if node.left:
                q.append([node.left, val1, val2])
            if node.right:
                q.append([node.right, val1, val2])
            
        return ret