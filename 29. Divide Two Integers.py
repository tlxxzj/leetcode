class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend ==0:
            return 0
        flag= 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            flag = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        d = {}
        for i in range(32):
            d[1<<i] = i
        f = []
        while divisor:
            x=divisor &(-divisor)
            f.append(d[x])
            divisor -=x
        
        l = 0
        r = dividend
        ret = 0
        while l<=r:
            m = (l + r) >> 1
            k = sum([m << i for i in f])
            if k <= dividend:
                l = m + 1
                ret = m
            else:
                r = m - 1
        if flag == -1:
            ret = -fet
        return min(ret, (1<<31)-1)
        