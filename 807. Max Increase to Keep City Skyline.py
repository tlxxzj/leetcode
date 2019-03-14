class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        row = [max(r) for r in grid]
        col = [0] * m
        for j in range(m):
            for i in range(n):
                col[j] = max(col[j], grid[i][j])
        ret = 0
        for i in range(n):
            for j in range(m):
                ret += max(0, min(row[i], col[j]) - grid[i][j])
        return ret
        