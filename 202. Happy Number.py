class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n not in nums:
            nums.add(n)
            m = 0
            while n > 0:
                x = n % 10
                n //= 10
                m += x * x
            n = m
        return n == 1