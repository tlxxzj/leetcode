class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        i, j = 0, 0
        ret = n + 1
        while i < j or j < n:
            if sum < target:
                if j < n:
                    sum += nums[j]
                    j += 1
                else:
                    break
            else:
                ret = min(ret, j - i)
                sum -= nums[i]
                i += 1
        if ret <= n:
            return ret
        return 0
