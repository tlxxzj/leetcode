# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def treehas(node, val):
            while node:
                if node.val == val: return True
                elif val < node.val: node = node.left
                else: node = node.right
            return False
        
        def find(node, val):
            if node:
                return (val != node.val*2 and treehas(root, val-node.val)) or find(node.left, val) or find(node.right, val)
            return False
        return find(root, k)
                