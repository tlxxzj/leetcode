class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        res = [[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                k = i*c + j
                res[i][j] = mat[k//n][k%n]
        
        return res
