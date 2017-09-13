# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (not root) or (not root.left):
            return -1
        
        def find(v, r):
            if r.val > v:
                return r.val
            elif r.left:
                x = find(v, r.left)
                y = find(v, r.right)
                if x==-1:
                    return y
                elif y==-1:
                    return x
                return min(x, y)
            else:
                return -1
        
        return find(root.val, root)
                