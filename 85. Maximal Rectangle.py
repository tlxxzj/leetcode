class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res = 0
        rows, cols = len(matrix), len(matrix[0])
        left = [[0] * (cols+1) for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "0":
                    continue
                left[i][j] = left[i][j-1] + 1
                width = left[i][j]
                for k in range(i, -1, -1):
                    width = min(width, left[k][j])
                    res = max(res, width * (i-k+1))
        return res