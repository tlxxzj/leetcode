class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = min(n, 10)
        ret = 0
        f=1
        for i in range(n):
            f *= 10 -i
            ret += f - f/10
        return ret + 1
    
        