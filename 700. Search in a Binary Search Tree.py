# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        while root != None and root.val != val:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                break
        return root
        