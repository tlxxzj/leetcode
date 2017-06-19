class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num ==0 : return '0'
        ret = ''
        sign = ''
        if num < 0:
            sign = '-'
            num = - num
        while num:
            ret = str(num%7) + ret
            num /= 7
        return sign + ret
        