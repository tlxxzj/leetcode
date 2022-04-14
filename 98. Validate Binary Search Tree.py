# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        dmax = {}
        dmin = {}
        def _max(node):
            if node in dmax:
                return dmax[node]
            ret = node.val
            if node.left:
                ret = max(ret, _max(node.left))
            if node.right:
                ret = max(ret, _max(node.right))
            dmax[node] = ret
            return ret
        def _min(node):
            if node in dmin:
                return dmin[node]
            ret = node.val
            if node.left:
                ret = min(ret, _min(node.left))
            if node.right:
                ret = min(ret, _min(node.right))
            dmin[node] = ret
            return ret
        
        def valid(node):
            if not node:
                return True
            if node.left and node.val <= _max(node.left):
                return False
            if node.right and node.val >= _min(node.right):
                return False
            return valid(node.left) and valid(node.right)
        
        return valid(root)

        

        