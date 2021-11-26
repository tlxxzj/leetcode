class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def lower_bound(nums, l, r, x):
            while l < r:
                m = (l + r) >> 1
                if nums[m] < x:
                    l = m + 1
                elif nums[m] >= x:
                    r = m
            return r

        n = len(nums)
        nums.sort()
        ret = nums[0] + nums[1] + nums[2]
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                x = target - (nums[i] + nums[j])
                k = lower_bound(nums, j+1, n, x)
                if k != n:
                    if nums[k] == x:
                        return target
                    if abs(target-nums[i]-nums[j]-nums[k]) < abs(target-ret):
                        ret = nums[i]+nums[j]+nums[k]
                    if k -1 > j and abs(target-nums[i]-nums[j]-nums[k-1]) < abs(target-ret):
                        ret = nums[i]+nums[j]+nums[k-1]
                elif abs(target-nums[i]-nums[j]-nums[k-1]) < abs(target-ret):
                    ret = nums[i]+nums[j]+nums[k-1]
        return ret
        