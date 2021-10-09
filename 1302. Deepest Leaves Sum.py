# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        nodes = [root]
        while len(nodes) > 0:
            nodes2 = []
            for node in nodes:
                if node.left:
                    nodes2.append(node.left)
                if node.right:
                    nodes2.append(node.right)
            if len(nodes2) == 0:
                break
            nodes = nodes2
        return sum([node.val for node in nodes])