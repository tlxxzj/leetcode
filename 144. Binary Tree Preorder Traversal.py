# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        q = [root]
        while len(q) > 0:
            node = q.pop()
            if node:
                ret.append(node.val)
                q.append(node.right)
                q.append(node.left)
        return ret
            