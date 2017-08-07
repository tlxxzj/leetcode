class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int((-1  + math.sqrt(1+4*2*n))/2)
