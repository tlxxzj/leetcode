class Solution:
    def get_max(self, g, m, n, x, y):
        if x < 0 or x >= m or y < 0 or y >= n or g[x][y] == 0:
            return 0
        t = g[x][y]
        g[x][y] = 0
        a = self.get_max(g, m, n, x+1, y)
        b = self.get_max(g, m, n, x-1, y)
        c = self.get_max(g, m, n, x, y+1)
        d = self.get_max(g, m, n, x, y-1)
        ret = max(a, b, c, d) + t
        g[x][y] = t
        return ret

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ret = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    ret = max(ret, self.get_max(grid, m, n, i, j))
        return ret