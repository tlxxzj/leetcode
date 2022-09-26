class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        x = 0
        for i in range(n+1):
            x ^= i
        for num in nums:
            x ^= num
        return x