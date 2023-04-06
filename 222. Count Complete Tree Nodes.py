# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ld, node = 0, root
        while node:
            ld += 1
            node = node.left
        rd, node = 0, root
        while node:
            rd += 1
            node = node.right
        if ld == rd:
            return (2 ** ld) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)