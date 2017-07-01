class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        get = lambda x, y:  float('inf') if x<0 or y<0 else grid[x][y]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:continue
                grid[i][j] += min(get(i-1, j), get(i, j-1))
        return grid[-1][-1]
        