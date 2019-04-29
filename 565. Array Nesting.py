class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ret = 0
        A = nums
        n = len(A)
        S = set([])
        for i in range(n):
            if A[i] in S:
                continue
            s = set([])
            x = i
            while A[x] not in s:
                s.add(A[x])
                S.add(A[x])
                x = A[x]
            ret = max(ret, len(s))
        return ret