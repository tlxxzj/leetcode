class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if (not matrix) or (not matrix[0]):
            return []
        m = len(matrix)
        n = len(matrix[0])
        ret = []
        k = 0
        while len(ret) < m*n:
            i, j = k, k
            while j < n-k:
                ret.append(matrix[i][j])
                j += 1
            
            i, j = k+1, n-k-1
            while i < m-k:
                ret.append(matrix[i][j])
                i += 1
            
            i, j = m-1-k, n-k-2
            while i>k and j >= k:
                ret.append(matrix[i][j])
                j -= 1
            
            i, j = m-1-k-1, k
            while i>k and j<n-k-1:
                ret.append(matrix[i][j])
                i -= 1
            
            k += 1
        
        return ret
            