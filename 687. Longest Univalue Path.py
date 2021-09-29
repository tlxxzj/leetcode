# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        ret = [0]
        def longestpath(node):
            if not node:
                return 0
            k = 1
            l, r = longestpath(node.left), longestpath(node.right)
            if node.left and node.left.val == node.val:
                k = max(k, l+1)
            else:
                l = 0
            if node.right and node.right.val == node.val:
                k = max(k, r+1)
            else:
                r = 0
            #print(l, r, k)
            ret[0] = max(ret[0], l+r)
            return k
        longestpath(root)
        return ret[0]
            