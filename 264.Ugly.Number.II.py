class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [1]
        f2, f3, f5 = 0, 0, 0
        while len(ret) <n :
            minnum = min(ret[f2] * 2, ret[f3]*3, ret[f5] * 5)
            if minnum == ret[f2] * 2:
                f2 += 1
            elif minnum == ret[f3]*3:
                f3 += 1
            else:
                f5 += 1
            if minnum > ret[-1]:
                ret.append(minnum)
        return ret[n-1]
        