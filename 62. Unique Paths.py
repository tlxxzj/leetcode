class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for j in range(n)] for i in range(m)]
        paths[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    paths[i][j] += paths[i-1][j]
                if j-1 >= 0:
                    paths[i][j] += paths[i][j-1]

        return paths[m-1][n-1]