class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0
        cnt = 0
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                cnt += 1
            else:
                ret += (1+cnt) * cnt // 2
                cnt = 0
        ret += (1+cnt) * cnt // 2
        return ret