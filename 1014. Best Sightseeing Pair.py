class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ret = 0
        n = len(A)
        i = 0
        for j in range(1, n):
            ret = max(ret, A[i] + A[j] + i - j)
            if A[j] + j >=  A[i] + i:
                i = j
        return ret