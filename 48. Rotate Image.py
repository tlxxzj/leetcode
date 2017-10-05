class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        n = len(matrix)
        k = 0
        while k*2 < n:
            ret = [matrix[k][i + k] for i in range(n - 2 * k)]
            ret2 = [matrix[i + k][n - 1 - k] for i in range(n - 2 * k)]
            ret3 = [matrix[n - 1 - k][n - 1 - k - i] for i in range(n - 2 * k)]
            print ret, ret2, ret3
            for i in range(n - 2 * k):
                matrix[k][i + k] = matrix[n - 1 - k - i][k]
            for i in range(n - 2 * k):
                matrix[i + k][n - 1 - k] = ret[i]
            for i in range(n - 2 * k):
                matrix[n - 1 - k][n - 1 - k - i] = ret2[i]
            for i in range(n - 2 * k):
                matrix[n - 1 - k - i][k] = ret3[i]
            k += 1
