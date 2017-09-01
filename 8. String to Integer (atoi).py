class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n = len(str)
        i = 0
        ret = 0
        flag = 0
        
        while i < n and str[i].isspace():
            i += 1
        
        if i < n and str[i] == '-':
            i +=1
            flag = 1
        elif i < n and str[i] == '+':
            i += 1
            flag = 2
        
        if i < n and str[i].isdigit():
            while i < n and str[i].isdigit():
                ret = ret * 10 + int(str[i])
                i += 1
        
        if flag == 1:
            ret = -ret
        
        if ret > 2147483647:
            ret = 2147483647
        elif ret < -2147483648:
            ret = -2147483648
        
        return ret
        