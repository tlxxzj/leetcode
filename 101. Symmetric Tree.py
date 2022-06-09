# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def getVal(node):
            if not node:
                return None
            return node.val
        
        def getNextLevel(nodes):
            ret = []
            for node in nodes:
                if node:
                    ret.append(node.left)
                    ret.append(node.right)
            return ret
        
        q1, q2 =[root.left], [root.right]
        while len(q1) > 0 or len(q2) > 0:
            if len(q1) != len(q2):
                return False
            n = len(q1)
            for i in range(n):
                if getVal(q1[i]) != getVal(q2[-i-1]):
                    return False
            q1, q2 = getNextLevel(q1), getNextLevel(q2)
        
        return True