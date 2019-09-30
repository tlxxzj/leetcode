class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n,m = len(A), len(A[0])
        ret = n*(1<<(m-1))
        for i in range(1, m):
            zero = 0
            for j in range(n):
                if A[j][0] + A[j][i] == 1:
                    zero += 1
            x = max(zero, n-zero)
            ret += x*(1<<(m-i-1))
        return ret
        