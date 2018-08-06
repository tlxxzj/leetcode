# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        
        def geth(root):
            if not root:
                return 0
            return max(geth(root.left), geth(root.right)) + 1
        
        H = geth(root)
        n = (2**H) - 1
        ret = [[""] * n for i in range(H)]
        
        def travel(root, ret, h, l, r):
            if not root:
                return
            m = (l + r) // 2
            ret[h][m] = str(root.val)
            travel(root.left, ret, h+1, l, m-1)
            travel(root.right, ret, h+1, m+1, r)
        travel(root, ret, 0, 0, n)
        return ret
        
        