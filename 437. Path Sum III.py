# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        from collections import defaultdict
        def path(node, sums):
            if not node:
                return 0
            sums2 = defaultdict(int)
            sums2[node.val] = 1
            for key, val in sums.items():
                sums2[key+node.val] += val
            return sums2.get(targetSum, 0) + path(node.left, sums2.copy()) + path(node.right, sums2.copy())
        return path(root, defaultdict(int))
            