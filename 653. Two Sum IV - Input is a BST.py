# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def iterInorder(node):
            if node:
                yield from iterInorder(node.left)
                yield node
                yield from iterInorder(node.right)
        
        def iterReverse(node):
            if node:
                yield from iterReverse(node.right)
                yield node
                yield from iterReverse(node.left)
        
        left, right = iterInorder(root), iterReverse(root)
        a, b = next(left), next(right)
        if a.val * 2 > k or b.val * 2 < k:
            return False
        while a != b:
            if a.val + b.val < k:
                a = next(left)
            elif a.val + b.val > k:
                b = next(right)
            else:
                return True
        return False
