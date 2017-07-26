class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ret = float('inf')
        sum, cnt = 0, 0
        for i in range(len(nums)):
            if nums[i] >= sum+nums[i]:
                sum, cnt = nums[i], 1
            else:
                sum += nums[i]
                cnt += 1
            if sum >= s:
                while sum>=s and cnt>=1:
                    ret = min(ret, cnt)
                    sum -= nums[i-cnt+1]
                    cnt -= 1
        return 0 if ret == float('inf') else ret
