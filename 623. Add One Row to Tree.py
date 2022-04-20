# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            node = TreeNode(val, root)
            return node
        
        row = [root]
        while depth > 2:
            row2 = []
            for node in row:
                if node.left:
                    row2.append(node.left)
                if node.right:
                    row2.append(node.right)
            row = row2
            depth -= 1
        
        for node in row:
            left,right = node.left, node.right
            node.left = TreeNode(val, left)
            node.right = TreeNode(val, None, right)
        
        return root
        