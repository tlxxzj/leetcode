# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preOrderTraversal(node):
            if not node:
                return None
            left, right = node.left, node.right
            node.left = None
            node.right = left
            if left:
                node = preOrderTraversal(left)
            node.right = right
            if right:
                node = preOrderTraversal(right)
            return node

        preOrderTraversal(root)


