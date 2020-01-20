class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if len(s1) != len(s2):
            return -1
        n = len(s1)
        x, y = 0, 0
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            if s1[i] == 'x':
                x += 1
            else:
                y += 1
        if (x + y)&1 == 1:
            return -1
        return (x >> 1) + (y >> 1) + (x % 2) + (y % 2)
        