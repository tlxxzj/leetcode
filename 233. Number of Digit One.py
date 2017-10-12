class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if n <=0:
            return 0
        if n < 10:
            return 1
        s = str(n)
        n = len(s)
        k = 1
        for i in range(n):
            k *= 10
        ret = 0
        for i in range(n):
            k /= 10
            if i == 0:
                l = 1
            else:
                l = int(s[:i]) + 1
            if i == n-1:
                r = 1
            else:
                r = int(s[i+1:]) + 1
            #print l, r, ret
            if s[i] == '1':
                ret += (l - 1) * k + r
            elif s[i] == '0':
                ret += (l - 1) * k
            else:
                ret += l * k
        return int(ret)
        