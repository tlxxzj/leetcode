class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = sum(A)
        cur = 0
        n = len(A)
        for i in range(n):
            cur += i*A[i]
        ret = cur
        for i in A:
            cur = cur-s+n*i
            ret = max(ret, cur)
        return ret
            