class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        r1 = [triangle[0][0]]
        r2 = [0, 0]
        for i in range(1, n):
            r2[0] = triangle[i][0] + r1[0]
            r2[-1] = triangle[i][-1] + r1[-1]
            for j in range(1, i):
                r2[j] = triangle[i][j] + min(r1[j], r1[j-1])
            r1 = r2
            r2 = [0] * (i+2)
        return min(r1)