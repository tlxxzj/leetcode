class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = m * (1 << (n - 1))
        for i in range(m):
            if grid[i][0] == 1:
                continue
            for j in range(n):
                grid[i][j] ^= 1
        for j in range(1, n):
            v = 0
            for i in range(m):
                 v += grid[i][j]
            ret += max(v, m-v) * (1 <<(n-1-j))
        return ret
