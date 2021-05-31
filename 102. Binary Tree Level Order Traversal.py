# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level_values = []
        nodes = [root]
        while len(nodes) > 0:
            values = []
            next_nodes = []
            for node in nodes:
                values.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            level_values.append(values)
            nodes = next_nodes
        return level_values