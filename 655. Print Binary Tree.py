# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getHeight(node):
            if not node: return 0
            return max(getHeight(node.left), getHeight(node.right)) + 1
        height = getHeight(root)
        m = height
        n = (1 << m) - 1
        #print(m, n)
        ret = []
        q = [(root, 0, n)] if height > 0 else []
        while len(q) > 0:
            q2 = []
            row = [''] * n
            for node, left, right in q:
                mid = (left + right) >> 1
                row[mid] = str(node.val)
                if node.left:
                    q2.append((node.left, left, mid-1))
                if node.right:
                    q2.append((node.right, mid+1, right))
            q = q2
            ret.append(row)
        return ret