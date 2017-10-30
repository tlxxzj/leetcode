class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        x = 1
        q = [float('inf')]
        ret = []
        for i in nums[:k]:
            while len(q) > x and i > q[-1]:
                q.pop()
            q.append(i)
        ret.append(q[x])
        for idx, i in enumerate(nums[k:], k):
            if q[x] == nums[idx-k]:
                x += 1
            while len(q) > x and i > q[-1]:
                q.pop()
            q.append(i)
            ret.append(q[x])
        return ret