class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        from copy import deepcopy
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        inx = [[0] * n for i in range(m)]
        out = [[0] * n for i in range(m)]
        cnt = [[1] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i-1>=0 and matrix[i][j] < matrix[i-1][j]:
                    inx[i-1][j] += 1
                    out[i][j] += 1
                if i+1<m and matrix[i][j] < matrix[i+1][j]:
                    inx[i+1][j] += 1
                    out[i][j] += 1
                if j-1>=0 and matrix[i][j] < matrix[i][j-1]:
                    inx[i][j-1] += 1
                    out[i][j] += 1
                if j+1<n and matrix[i][j] < matrix[i][j+1]:
                    inx[i][j+1] += 1
                    out[i][j] += 1
        q1 = []
        for i in range(m):
            for j in range(n):
                if inx[i][j] == 0:
                    q1.append([i, j])
        
        ret = 0
        while len(q1) > 0:
            t = q1.pop()
            i, j = t
            ret = max(ret, cnt[i][j])
            if i-1>=0 and matrix[i][j] < matrix[i-1][j]:
                inx[i-1][j] -= 1
                if inx[i-1][j] == 0:
                    q1.append([i-1, j])
                cnt[i-1][j] = max(cnt[i-1][j], cnt[i][j]+1)
            if i+1<m and matrix[i][j] < matrix[i+1][j]:
                inx[i+1][j] -= 1
                if inx[i+1][j]==0:
                    q1.append([i+1, j])
                cnt[i+1][j] = max(cnt[i+1][j], cnt[i][j]+1)
            if j-1>=0 and matrix[i][j] < matrix[i][j-1]:
                inx[i][j-1] -= 1
                if inx[i][j-1]==0:
                    q1.append([i, j-1])
                cnt[i][j-1] = max(cnt[i][j-1], cnt[i][j]+1)
            if j+1<n and matrix[i][j] < matrix[i][j+1]:
                inx[i][j+1] -= 1
                if inx[i][j+1]==0:
                    q1.append([i,j+1])
                cnt[i][j+1] = max(cnt[i][j+1], cnt[i][j]+1)
        
        return ret
        
        
                    
        
        