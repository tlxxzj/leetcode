class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        def getN(num):
            x = num
            cnt = 0
            i = 0
            while x >= 10:
                x = x // 10
                cnt += 9 * (10 ** i) * (i + 1)
                i += 1
            cnt += (num + 1 - 10 ** i) * (i+1)
            return cnt
        
        l, r = 1, 1<<31
        while l < r:
            m = (l + r) >> 1
            x = getN(m)
            if x < n:
                l = m + 1
            elif x > n:
                r = m
            else:
                return m % 10
        y = n - getN(l-1)
        return int(str(l)[y-1])
        
            