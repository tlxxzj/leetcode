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
        :rtype: List[List[int]]
        """
        ret = []
        def path(node, l, s):
            l.append(node.val)
            s -= node.val
            if node.left is None and node.right is None:
                if s == 0:
                    ret.append(l[:])
            else:
                if node.left:
                    path(node.left, l, s)
                if node.right:
                    path(node.right, l, s)
            l.pop()
            
        if root:
            path(root, [], sum)
        return ret