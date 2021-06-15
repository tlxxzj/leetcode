# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        q = []
        
        def append_nodes(node: TreeNode):
            while node:
                q.append(node)
                node = node.left
        
        append_nodes(root)
        while len(q) > 0:
            node = q.pop()
            if (k := k-1) == 0:
                return node.val
            append_nodes(node.right)
    