class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = []
        negative = False
        if num < 0:
            negative = True
            num = -num
        
        while num > 0:
            res.append(str(num%7))
            num //= 7
        
        res.reverse()
        if negative:
            return "-" + "".join(res)
        return "".join(res)
