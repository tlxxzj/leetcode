# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        import heapq
        def traverse(node):
            q = []
            while node:
                q.append(node)
                node = node.left
            while len(q) > 0:
                x = q.pop()
                yield x.val
                node = x.right
                while node:
                    q.append(node)
                    node = node.left
        
        a, b = traverse(root1), traverse(root2)
        return list(heapq.merge(a, b))