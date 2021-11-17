# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ret = [] if root.val in to_delete else [root]
        def getForest(node):
            if not node:
                return None
            node.left = getForest(node.left)
            node.right = getForest(node.right)
            if node.val in to_delete:
                if node.left and (node.left not in to_delete):
                    ret.append(node.left)
                if node.right and (node.right not in to_delete):
                    ret.append(node.right)
                return None
            return node
        getForest(root)
        return ret
