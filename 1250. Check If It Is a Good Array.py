class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a, b):
            if a%b == 0:
                return b
            return gcd(b, a%b)
        g = nums[0]
        for num in nums:
            g = gcd(g, num)
        return g == 1