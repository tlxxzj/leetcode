# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def depth(node):
            if not node:
                return 0
            else:
                return 1 + max(depth(node.left), depth(node.right))
        
        def find_node(node, depth, max_depth):
            if node:
                if depth == max_depth:
                    return node
                else:
                    l = find_node(node.left, depth+1, max_depth)
                    r = find_node(node.right, depth+1, max_depth)
                    if l and r:
                        return node
                    if l:
                        return l
                    if r:
                        return r
                    return None
            else:
                return None
        
        max_depth = depth(root)
        node = find_node(root, 1, max_depth)
        
        return node
        
        