class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        if stones[1] != 1:
            return False
        dp = {}
        for i in stones:
            dp[i] = []
        dp[1].append(1)
        for i in stones:
            for st in dp[i]:
                for k in [-1, 0, 1]:
                    x = i + st + k
                    if x in dp:
                        y = st + k
                        if y not in dp[x]:
                            dp[x].append(y)

        return len(dp[stones[-1]]) > 0
        