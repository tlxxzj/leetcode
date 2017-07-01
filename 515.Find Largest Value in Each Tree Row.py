# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        st = []
        if root:
            st = [root]
        while len(st)>0:
            st2 = []
            mx = st[0].val
            for t in st:
                mx=max(mx, t.val)
                if t.left:
                    st2.append(t.left)
                if t.right:
                    st2.append(t.right)
            st = st2
            ret.append(mx)
                
        return ret
        