class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i in range(0, len(nums)):
            if d.get(nums[i], 0)>0:
                return True
            d[nums[i]] = d.get(nums[i], 0)+1
            if i>=k:
                d[nums[i-k]] -= 1
        return False
        