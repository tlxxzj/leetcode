class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        for i in xrange(0, int(math.sqrt(c))+1):
            x=i*i
            y=int(math.sqrt(c-x))
            y=y*y
            if x+y == c: 
                return True
        return False
        