class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ret = nums[0] + nums[1] + nums[2]
        for i in range(0, n-2):
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(target -s) < abs(target-ret):
                    ret = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return target
        return ret