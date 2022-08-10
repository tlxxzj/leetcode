# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        q = []
        node = root
        while node:
            q.append(node)
            node = node.left
        pre = None
        while len(q) > 0:
            node = q[-1]
            if node.right != pre:
                node = node.right
                while node:
                    q.append(node)
                    node = node.left
                pre = None
            else:
                pre = q.pop()
                ret.append(pre.val)
        return ret