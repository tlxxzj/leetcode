# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ret = [True]
        def balance(node):
            if node is None: return 0
            lh = balance(node.left)
            rh = balance(node.right)
            if abs(lh - rh) > 1:
                ret[0] = False
            return max(lh, rh) + 1
        balance(root)
        return ret[0]
            
        