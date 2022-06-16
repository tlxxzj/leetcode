# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        ret = [True]

        def getH(node):
            if (not node) or (not ret[0]):
                return 0
            l, r = getH(node.left), getH(node.right)
            if abs(l-r)>1:
                ret[0] = False
            return max(l, r) + 1
        
        getH(root)
        return ret[0]