# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ret = []
        q = [(root, str(root.val))]
        while len(q) > 0:
            node, path = q.pop()
            if (not node.left) and (not node.right):
                ret.append(path)
            if node.left:
                q.append((node.left, f'{path}->{node.left.val}'))
            if node.right:
                q.append((node.right, f'{path}->{node.right.val}'))
        return ret

