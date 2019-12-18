from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if (not nums1) or (not nums2):
            return []
        ret = []
        for a in nums1:
            for b in nums2:
                heappush(ret, (-(a+b), (a, b)))
                if len(ret) > k:
                    heappop(ret)
        ret = [i[1] for i in ret]
        return ret