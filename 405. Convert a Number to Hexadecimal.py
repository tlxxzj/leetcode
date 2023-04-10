class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hexstr = "0123456789abcdef"
        if num < 0:
            num = (1<<32) + num
        ret = []
        while num > 0:
            x = num % 16
            ret.append(hexstr[x])
            num = num // 16
        ret.reverse()
        return "".join(ret)
        

