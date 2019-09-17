# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def get_depth(node):
            if node is None:
                return 0
            return 1 + max(get_depth(node.left), get_depth(node.right))
        
        depth = get_depth(root)
        def get_lca(node, d):
            if node:
                if d == depth:
                    return node
                else:
                    l,r = get_lca(node.left, d+1), get_lca(node.right, d+1)
                    if l and r:
                        return node
                    elif l:
                        return l
                    elif r:
                        return r
            return None
        
        node = get_lca(root, 1)
        return node