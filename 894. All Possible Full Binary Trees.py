# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        #from copy import deepcopy
        if N % 2 == 0:
            return []
        dp = [[] for i in range(N + 1)]
        dp[1] = [TreeNode(0)]
        for i in range(3, N + 1):
            for j in range(1, i, 2):
                for left in dp[j]:
                    for right in dp[i - 1 - j]:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        dp[i].append(root)
        return dp[N]
                
        
        