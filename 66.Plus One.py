class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        s = 1
        for i in range(len(digits)):
            s = s + digits[i]
            digits[i] = s%10
            s /= 10
        if s > 0:
            digits.append(s)
        return digits[::-1]
