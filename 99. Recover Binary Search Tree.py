# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        left, right = None, None
        n1, n2 = None, None
        q = []
        node = root
        while node:
            q.append(node)
            node = node.left
        
        while len(q) > 0:
            node = q.pop()
            n1, n2 = n2, node
            if n1 and n1.val > n2.val:
                if not left:
                    left, right = n1, n2
                else:
                    right = n2
                    left.val, right.val = right.val, left.val
                    break
            
            node = node.right
            while node:
                q.append(node)
                node = node.left
        
        if left.val > right.val:
            left.val, right.val = right.val, left.val

        

            


