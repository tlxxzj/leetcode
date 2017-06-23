# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self._rob(root, True)
    
    def _rob(self, root, canbuy):
        if root is None: return 0
        ret = 0
        if canbuy:
            buy, nobuy = 0, 0
            if hasattr(root, 'buy'):
                buy = root.buy
            else:
                buy = root.val + self._rob(root.left, False) + self._rob(root.right, False)
                root.buy = buy
            if hasattr(root, 'nobuy'):
                nobuy = root.nobuy
            else:
                nobuy = self._rob(root.left, True) + self._rob(root.right, True)
                root.nobuy = nobuy
            ret = max(buy, nobuy)
        else:
            ret = self._rob(root.left, True) + self._rob(root.right, True)
        return ret
