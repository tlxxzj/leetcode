class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def binSearch(arr, target):
            l, r = 0, len(arr)
            while l < r:
                m = (l+r)/2
                if arr[m] < target:
                    l = m + 1
                else:
                    r = m
            return l

        ret = 0
        s = 0
        n = len(nums)
        index = {0: [0]}
        sums = [0] * n
        for i in range(n):
            s += nums[i]
            sums[i] = s
            if s in index:
                index[s].append(i+1)
            else:
                index[s] = [i+1]
        for i in range(n):
            x = sums[i] - k
            ret += binSearch(index.get(x, []), i+1)
        return ret
