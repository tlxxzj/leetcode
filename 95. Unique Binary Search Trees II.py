# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(l, r):
            if l > r:
                return [None]
            if l == r:
                return [TreeNode(l)]
            trees = []
            for i in range(l, r+1):
                left, right = generate(l, i-1), generate(i+1, r)
                trees.extend([TreeNode(i, n1, n2) for n1 in left for n2 in right])
            return trees
        
        return generate(1, n)
        
