class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0
        nums = [1] * n
        nums[0] = nums[1] = 0
        for i in range(n):
            if nums[i] == 0: continue
            x = i + i
            while x < n:
                nums[x] = 0
                x += i
        return sum(nums)
        