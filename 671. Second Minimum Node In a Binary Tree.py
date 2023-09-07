# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        rootval = root.val
        res = [-1]
        
        def find(node):
            if node.val > rootval and (res[0] == -1 or node.val < res[0]):
                res[0] = node.val
            
            if node.val == rootval and node.left:
                    find(node.left)
                    find(node.right)
        
        find(root)

        return res[0]
