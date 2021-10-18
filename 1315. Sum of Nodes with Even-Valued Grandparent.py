# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = [[root, None, None]] if root else []
        s = 0
        while len(q) > 0:
            node, parent, grandparent = q.pop()
            if grandparent and (grandparent.val & 1) == 0:
                s += node.val
            if node.left:
                q.append([node.left, node, parent])
            if node.right:
                q.append([node.right, node, parent])
        return s