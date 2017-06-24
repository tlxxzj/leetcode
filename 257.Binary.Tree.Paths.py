# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        def treePath(node, path):
            if node is None: return
            if node.left is None and node.right is None:
                paths.append(path)
                return
            if node.left:
                treePath(node.left, path + '->' + str(node.left.val))
            if node.right:
                treePath(node.right, path + '->' + str(node.right.val))
        if root:
            treePath(root, str(root.val))
        return paths