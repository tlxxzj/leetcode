class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ret = []
        s = '123456789'
        lena, lenb = len(str(low)), len(str(high))
        for i in range(lena, lenb+1):
            for j in range(0, 10-i):
                x = int(s[j:j+i])
                if low <= x and x <= high:
                    ret.append(x)
                elif x > high:
                    break
        return ret