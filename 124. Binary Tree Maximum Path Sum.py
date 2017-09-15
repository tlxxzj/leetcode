# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ninf = -float('inf')
        ret = [ninf]
        def path(root):
            if not root:
                return ninf
            l= path(root.left)
            r = path(root.right)
            y = root.val
            if l>0:
                y+=l
            if r>0:
                y+=r
            ret[0]=max(ret[0], y)
            return max(root.val, max(root.val+l, root.val+r))
        
        path(root)
        return ret[0]
        