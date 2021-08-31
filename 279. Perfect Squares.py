class Solution:
    def getSquares(self, n):
        ret = []
        for i in range(1, n):
            if i*i <= n:
                ret.append(i*i)
            else:
                break
        return ret
    
    def numSquares(self, n: int) -> int:
        squares = self.getSquares(n)
        dp = [n] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            for s in squares:
                if i-s >= 0:
                    dp[i] = min(dp[i], dp[i-s]+1)
                else:
                    break
        #print(dp)
        return dp[n]