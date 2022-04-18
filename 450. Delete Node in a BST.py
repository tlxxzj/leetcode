# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertNode(self, root, node):
        if not root:
            return node
        if not node:
            return root
        if node.val < root.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
        return root
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return root
        if root.val == key:
            ret = self.insertNode(root.left, root.right)
            root.left = None
            root.right = None
            return ret
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root