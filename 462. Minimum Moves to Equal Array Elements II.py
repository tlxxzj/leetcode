class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        x = nums[n // 2]
        return sum([abs(num-x) for num in nums])