class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        sub = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                sub += 1
                res = max(res, sub)
            else:
                sub = 1
        return res
