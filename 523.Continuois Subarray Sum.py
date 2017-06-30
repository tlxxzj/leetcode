class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        for i in range(1, len(nums)):
            if nums[i-1] == 0 and nums[i] == 0:
                return True
        if k == 0: return False
        k=abs(k)
        sumSet = set()
        s = 0
        pre = 0
        for i in nums:
            s += i
            s %= k
            if s in sumSet:
                return True
            sumSet.add(pre)
            pre = s
        return False
            