class Solution:
    def is_close(self, grid, n, m, x, y):
        ret = 1
        q = [(x, y)]
        while len(q) > 0:
            a, b = q.pop()
            if a < 0 or a >= n or b < 0 or b >= m or grid[a][b] != 0: continue
            if a == 0 or a == n-1 or b == 0 or b == m - 1: ret = 0
            grid[a][b] = 1
            q.append((a+1, b))
            q.append((a-1, b))
            q.append((a, b+1))
            q.append((a, b-1))
        return ret

    def closedIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    ret += self.is_close(grid, n, m, i, j)
        return ret