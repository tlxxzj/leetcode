class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x == 0 or y == 0:
            return x == z or y == z
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        
        g = gcd(x, y)
        return z <= x + y and z % g == 0
        