# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        count = {}
        def walk(node):
            if not node:
                return 0
            s = node.val + walk(node.left) + walk(node.right)
            count[s] = count.get(s, 0) + 1
            return s
        ret = []
        cnt = -1
        walk(root)
        for k, v in count.iteritems():
            if v > cnt:
                ret = [k]
                cnt = v
            elif v == cnt:
                ret.append(k)
        return ret
            
        