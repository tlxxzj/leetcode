# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        ret = []
        q = []
        if root:
            q.append(root)
        
        while len(q) > 0:
            q2 = []
            val = q[0].val
            for node in q:
                val = max(val, node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q = q2
            ret.append(val)
        
        return ret