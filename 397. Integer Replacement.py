class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret=0
        while n>1:
            if n&1:
                ret += 1
                if n>3 and n&2:
                    n +=1
                else:
                    n -= 1
            else:
                n >>= 1
                ret += 1
        return ret
        