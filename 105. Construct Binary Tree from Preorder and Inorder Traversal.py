# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index = {}
        for i, num in enumerate(inorder):
            index[num] = i
        
        def build(i, j, l, r):
            if i>j or l >r:
                return None
            k = index[preorder[i]]
            n = k - l
            node = TreeNode(preorder[i])
            node.left = build(i+1, i+n, l, k-1)
            node.right = build(i+n+1, j, k+1, r)
            return node
        
        return build(0, len(preorder)-1, 0, len(preorder)-1)