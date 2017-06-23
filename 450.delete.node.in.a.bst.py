# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        return self._remove(root, key)
    
    def _min(self, node):
        while node.left:
            node = node.left
        return node.val
    
    def _remove(self, node, key):
        if node is None: return None
        ret = node
        if key < node.val:
            node.left = self._remove(node.left, key)
        elif key > node.val:
            node.right = self._remove(node.right, key)
        else:
            if node.left and node.right:
                node.val = self._min(node.right)
                node.right = self._remove(node.right, node.val)
            elif node.left:
                ret = node.left
            elif node.right:
                ret = node.right
            else:
                ret = None
        return ret