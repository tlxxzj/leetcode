class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2 ,l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[False] * (l2 + 1) for i in range(l1 + 1)]
        dp[0][0] = True
        for i in xrange(l1+1):
            for j in xrange(l2+1):
                k = i + j
                if dp[i][j]:
                    if i<l1 and s1[i] == s3[k]:
                        dp[i+1][j] = True
                    if j<l2 and s2[j] == s3[k]:
                        dp[i][j+1] = True
        
        return dp[l1][l2]
        
        