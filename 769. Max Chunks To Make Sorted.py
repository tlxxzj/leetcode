class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ret = 0
        start = 0
        minp, maxp = -1, -1
        for i, e in enumerate(arr, 0):
            if minp == -1:
                minp, maxp = arr[i], arr[i]
            else:
                minp = min(minp, e)
                maxp = max(maxp, e)
            if minp == start and maxp == i:
                ret += 1
                start = i + 1
                minp, maxp = -1, -1
        return ret