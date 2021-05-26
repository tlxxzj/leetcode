class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[0 for j in range(n)] for i in range(m)]
        paths[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i-1 >= 0:
                    paths[i][j] += paths[i-1][j]
                if j-1 >= 0:
                    paths[i][j] += paths[i][j-1]
        return paths[-1][-1]