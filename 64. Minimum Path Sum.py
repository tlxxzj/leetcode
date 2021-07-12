class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        inf = float('inf')
        sum = [[inf for j in range(n)] for i in range(m)]
        sum[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i-1>=0:
                    sum[i][j] = min(sum[i][j], sum[i-1][j] + grid[i][j])
                if j-1>=0:
                    sum[i][j] = min(sum[i][j], sum[i][j-1] + grid[i][j])
        return sum[-1][-1]