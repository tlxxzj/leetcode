
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        st = []
        pre = None
        if root:
            ret = [root]
        while len(st)>0:
            root = st.pop()
            if (root.left is None and root.right is None) or (pre is not None and (pre == root.left or pre == root.right)):
                ret.append(root.val)
                pre = root
            else:
                ret.append(root.right)
                ret.append(root.left)
        return ret
