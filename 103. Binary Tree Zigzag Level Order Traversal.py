# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ret = []
        left = True
        q = [root]
        while len(q) > 0:
            if left:
                ret.append([node.val for node in q])
            else:
                ret.append([node.val for node in reversed(q)])
            q2 = []
            for node in q:
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            left = not left
            q = q2
        return ret
        