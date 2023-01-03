# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ret = [None]

        def count(node):
            if ret[0] or (not node):
                return 0
            x = 0
            if node == p or node == q:
                x = 1
            y =  x + count(node.left) + count(node.right)
            if y == 2 and (not ret[0]):
                ret[0] = node
            return y
        count(root)
        return ret[0]