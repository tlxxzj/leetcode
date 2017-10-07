class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        k, c = 1, 9
        while n > k * c:
            n -= k * c
            k += 1
            c *= 10
        x = n / k
        y = n - x * k
        #print x, y
        if y == 0:
            x = x + c / 9 - 1
            return int(str(x)[-1])
        else:
            x = x + c / 9
            return int(str(x)[y - 1])
        