class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        res = 0
        mod = 10**9 + 7

        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
        dp = [[[0] *n for _ in range(m)] for _ in range(maxMove+1)]
        dp[0][startRow][startColumn] = 1

        for k in range(maxMove):
            for i in range(m):
                for j in range(n):
                    for x, y in moves:
                        x, y = x+i, y+j
                        if x <0 or x>=m or y<0 or y>=n:
                            res = (res + dp[k][i][j]) % mod
                        else:
                            dp[k+1][x][y] = (dp[k+1][x][y] + dp[k][i][j]) % mod
                    
        return res