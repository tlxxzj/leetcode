# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:   
        if not root:
            return False
        
        def issub(n1, n2):
            if n1 == None and n2 == None:
                return True
            if (n1 == None) != (n2 == None):
                return False
            if n1.val != n2.val:
                return False
            return issub(n1.left, n2.left) and issub(n1.right, n2.right)
        
        return issub(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
