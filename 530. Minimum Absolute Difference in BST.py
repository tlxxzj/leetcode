# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inOrder(node):
            if node.left:
                yield from inOrder(node.left)
            yield node.val
            if node.right:
                yield from inOrder(node.right)
        
        pre = -1
        ret = float('inf')
        for val in inOrder(root):
            if pre !=-1:
                ret = min(ret, abs(val - pre))
            pre = val
        return ret


