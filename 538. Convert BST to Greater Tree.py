# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bst(node, val):
            retVal = node.val
            node.val += val
            if node.right:
                x = bst(node.right, val)
                retVal += x
                node.val += x
            if node.left:
                retVal += bst(node.left, node.val)
            return retVal
        if root:
            bst(root, 0)
        return root