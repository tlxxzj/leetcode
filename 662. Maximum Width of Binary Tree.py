# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = [(root, 0)]
        while len(q) > 0:
            if len(q) == 1:
                res = max(res, 1)
            else:
                res = max(res, q[-1][1]-q[0][1]+1)
            
            q2 = []
            for node, x in q:
                if node.left:
                    q2.append((node.left, x*2-1))
                if node.right:
                    q2.append((node.right, x*2))
            
            q = q2
        
        return res
