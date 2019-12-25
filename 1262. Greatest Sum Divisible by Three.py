class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        a, b = [0,0,0], [0,0,0]
        ret = 0
        for num in nums:
            b = a[:]
            for x in a:
                y = num + x
                z = y % 3
                b[z] = max(b[z], y)
            ret = max(ret, b[0])
            a = b
        return ret