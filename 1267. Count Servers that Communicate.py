class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [0] * m
        ret = 0
        for i in range(m):
            s = sum(grid[i])
            if s > 1:
                ret += s
                row[i] = 1
        for j in range(n):
            s = 0
            s2 = 0
            for i in range(m):
                s += grid[i][j]
                s2 += grid[i][j] & row[i]
            if s > 1:
                ret += s - s2
        return ret
