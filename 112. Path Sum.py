# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        q = []
        if root:
            q = [(root, root.val)]
        while len(q) > 0:
            q2 = []
            for node, val in q:
                if (val == targetSum) and (not node.left) and (not node.right):
                    return True
                if node.left:
                    q2.append((node.left, val+node.left.val))
                if node.right:
                    q2.append((node.right, val+node.right.val))
            q = q2
        
        return False