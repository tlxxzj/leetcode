class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = abs(x)
        ret = 0
        while y != 0:
            ret = ret * 10 + y % 10
            y /= 10
        if x < 0:
            ret = -ret
        if ret > 0x7fffffff or ret < -0x80000000:
            return 0
        return ret
        