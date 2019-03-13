# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def tree(preorder, l, r):
            if l > r:
                return None
            root = TreeNode(preorder[l])
            k = l + 1
            while k <= r and preorder[k] < preorder[l]:
                k += 1
                
            root.left = tree(preorder, l+1, k-1)
            root.right = tree(preorder, k, r)
            return root
        
        return tree(preorder, 0, len(preorder)-1)

        