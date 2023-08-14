# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = [root]
        while len(q) > 0:
            val = 0
            q2 = []
            for node in q:
                val += node.val
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            res.append(val/len(q))
            q = q2
        return res
