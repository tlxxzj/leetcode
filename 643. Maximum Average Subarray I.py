class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ret = -float('inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if i+1<k:
                pass
            elif i+1==k:
                ret = max(ret, sum*1.0/k)
            else:
                sum -= nums[i-k]
                ret = max(ret, sum*1.0/k)
        return ret