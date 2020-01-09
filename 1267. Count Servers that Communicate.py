class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        row = [0] * m
        col = [0] * n
        ret = 0
        for i in range(m):
            for j in range(n):
                row[i] += grid[i][j]
                col[j] += grid[i][j]
                ret += grid[i][j]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    ret -= 1
        return ret