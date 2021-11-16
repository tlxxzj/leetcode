class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
       n = len(matrix)
       r1, r2 = [0] * n, [0] * n
       for row in matrix:
           for i in range(n):
               r2[i] = r1[i] + row[i]
               if i > 0:
                   r2[i] = min(r2[i], row[i] + r1[i-1])
               if i < n - 1:
                   r2[i] = min(r2[i], row[i] + r1[i+1])
           r1, r2 = r2, r1
       return min(r1)