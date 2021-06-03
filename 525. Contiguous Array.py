class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        min_nums = {0: -1}
        n = len(nums)
        if nums[0] == 0:
            nums[0] = -1
            min_nums[-1] = 0
        else:
            min_nums[1] = 0
        for i in range(1, n):
            num = nums[i]
            if num == 0:
                num = -1
            nums[i] = num + nums[i-1]
            if nums[i] in min_nums:
                ans = max(ans, i-min_nums[nums[i]])
            else:
                min_nums[nums[i]] = i
        return ans