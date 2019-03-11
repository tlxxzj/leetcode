# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        f = {}
        q = [root]
        while len(q) > 0:
            r = q.pop()
            if r.left:
                f[r.left] = r
                q.append(r.left)
            if r.right:
                f[r.right] = r
                q.append(r.right)
        
        q = [target]
        visited = set()
        visited.add(target)
        visited.add(None)
        while K > 0 and len(q) > 0:
            K -= 1
            q2 = []
            for node in q:
                if node.left not in visited:
                    q2.append(node.left)
                    visited.add(node.left)
                if node.right not in visited:
                    q2.append(node.right)
                    visited.add(node.right)
                if f.get(node, None) not in visited:
                    q2.append(f[node])
                    visited.add(f[node])
            q = q2
        
        return [node.val for node in q]

            
        