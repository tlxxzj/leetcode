# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        f = {}
        q = [root]
        leaf = []
        while len(q) > 0:
            r = q.pop()
            child = 0
            if r.left:
                f[r.left] = r
                q.append(r.left)
                child += 1
            if r.right:
                f[r.right] = r
                q.append(r.right)
                child += 1
            if child == 0:
                leaf.append(r)
        leaf.sort(key=lambda x: x.val)
        strs = []
        for r in leaf:
            if r.val != leaf[0].val:
                break
            s = []
            while r:
                s.append(chr(r.val + ord('a')))
                r = f.get(r, None)
            strs.append(''.join(s))
        
        strs.sort()
        return strs[0]