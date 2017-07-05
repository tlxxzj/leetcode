# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def path(root, sums):
            if root is None: return 0
            ret = sums.count(sums[-1]+root.val-sum)
            sums.append(sums[-1]+root.val)
            ret += path(root.left, sums) + path(root.right, sums)
            sums.pop()
            return ret
        return path(root, [0])