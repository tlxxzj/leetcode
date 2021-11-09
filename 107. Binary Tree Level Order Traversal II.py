# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        q = [root] if root else []
        ret =[]
        while len(q) > 0:
            q2 = []
            vals = []
            for node in q:
                vals.append(node.val)
                if node.left: q2.append(node.left)
                if node.right: q2.append(node.right)
            ret.append(vals)
            q = q2
        ret.reverse()
        return ret