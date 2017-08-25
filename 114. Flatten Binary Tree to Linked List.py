# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """# Definition for a binary tree node.
        def flatten(root):
            nil = None
            if root == nil: return [None, None]
            ret = [root, root]
            l = flatten(root.left)
            r = flatten(root.right)
            root.left = root.right = nil
            if l[0] == nil and r[0] == nil:
                pass
            elif l[0] == nil:
                root.right, r[0].left = r[0], nil
                ret[1] = r[1]
            elif r[0] == nil:
                root.right, l[0].left = l[0], nil
                ret[1] = l[1]
            else:
                root.right, l[0].left = l[0], nil   
                l[1].right, r[0].left = r[0], nil
                ret[1] = r[1]
            return ret
        root = flatten(root)
        
        