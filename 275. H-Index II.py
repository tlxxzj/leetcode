class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n
        while l < r:
            m = (l + r) >> 1
            if citations[m] < n - m:
                l = l + 1
            else:
                r = m
        return n - r