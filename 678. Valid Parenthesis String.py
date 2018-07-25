class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        dp = [True]
        dp[0] = True
        dp2 = []
        for i, c in enumerate(s, 1):
            if c == '(':
                dp2 = [False] + dp                
            elif c == ')':
                dp2 = dp[1:] + [False, False]
            else:
                x = [False] + dp
                y = dp[1:] + [False, False]
                z = dp + [False]
                dp2 = [x[i] or y[i] or z[i] for i in range(i+1)]
            dp = dp2
        return dp[0]
