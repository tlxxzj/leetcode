class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        m = len(primes)
        f = [0] * m
        ret = [1]
        while len(ret) < n:
            mi = float('inf')
            for i in range(m):
                num = ret[f[i]]*primes[i]
                while num <= ret[-1]:
                    f[i] += 1
                    num = ret[f[i]]*primes[i]
                mi = min(mi, num)
            ret.append(mi)
        return ret[n-1]
    