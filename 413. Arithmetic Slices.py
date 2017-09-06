class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        
        ret = 0
        i = 2
        k = 0
        diff = A[1] - A[0]
        
        while i < n:
            d = A[i] - A[i - 1]
            if diff == d:
                ret += (i-k+1)-2
            else:
                diff = d
                k = i - 1
            i += 1
        
        return ret