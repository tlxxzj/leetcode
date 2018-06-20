# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        root, val = self._prune(root)
        return root

    def _prune(self, root):
    	if root is None:
    		return root, 0
    	
    	lnode, lval = self._prune(root.left)
    	root.left = lnode
    	rnode, rval = self._prune(root.right)
    	root.right = rnode
    	val = root.val + lval + rval
    	if val == 0:
    		root = None
    	return root, val