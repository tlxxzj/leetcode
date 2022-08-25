class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n > 0:
            n -= n&-n
            ret += 1
        return ret