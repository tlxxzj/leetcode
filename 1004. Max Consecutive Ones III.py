class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        i, j = 0, 0
        zero = 0
        ret = 0
        while j < n:
            if A[j] == 0:
                zero += 1
            while i < j and zero > K:
                if A[i] == 0:
                    zero -= 1
                i += 1
            if zero <= K:
                ret = max(ret, j-i+1)
            j += 1
        return ret