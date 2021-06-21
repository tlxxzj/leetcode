# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ret = []
        q = []
        if root:
            q = [[root.val, root, [root.val]]]
        while len(q) > 0:
            q2 = []
            for sum, node, path in q:
                if (sum == targetSum) and (not node.left) and (not node.right):
                    ret.append(path)
                else:
                    if node.left:
                        q2.append([sum+node.left.val, node.left, path[:] + [node.left.val]])
                    if node.right:
                        path.append(node.right.val)
                        q2.append([sum+node.right.val, node.right, path])
            q = q2
        return ret