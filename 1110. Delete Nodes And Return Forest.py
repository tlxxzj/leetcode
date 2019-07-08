# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ret = []
        dels = set(to_delete)
        q = [root]
        if root.val not in dels:
            ret.append(root)
        while len(q) > 0:
            node = q.pop()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node.val in dels:
                if node.left and node.left.val not in dels:
                    ret.append(node.left)
                if node.right and node.right.val not in dels:
                    ret.append(node.right)
            if node.left and node.left.val in dels:
                node.left = None
            if node.right and node.right.val in dels:
                node.right = None
            
        return ret