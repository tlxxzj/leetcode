class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k >= n or k >= n - num.count('0'):
            return '0'
        ret = []
        for i in range(n):
            if num[i] == '0' and k >= len(ret):
                k -= len(ret)
                ret = []
                continue
            while k > 0 and len(ret) > 0 and num[i] < ret[-1]:
                k -= 1
                ret.pop()
            ret.append(num[i])
        ret = ''.join(ret)
        if k > 0:
            ret = ret[:-k]
        return ret