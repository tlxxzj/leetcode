class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        ret = 0
        for i in range(n):
            if n-i >= citations[i]:
                ret = max(ret, citations[i])
            else:
                ret = max(ret, n-i)
        return ret