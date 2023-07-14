class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        i, j = 0, 0
        while len(res) < m * n:
            while i >=0 and j < n:
                res.append(mat[i][j])
                i -= 1
                j += 1
            i += 1
            j -= 1
            if j + 1 < n:
                j += 1
            else:
                i += 1
            
            while i < m and j>=0:
                res.append(mat[i][j])
                i += 1
                j -= 1
            i -= 1
            j += 1
            if i + 1 < m:
                i += 1
            else:
                j += 1
        return res