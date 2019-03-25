class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        if n <= 1:
            return n
        ret = 1
        
        le = 0
        s = 0
        for i in range(1, n):
            if le == -1:
                if A[i] < A[i-1]:
                    le = -1
                    s = 2
                elif A[i] > A[i-1]:
                    le = 1
                    s += 1
                else:
                    le = s = 0
            elif le == 1:
                if A[i] < A[i-1]:
                    le = -1
                    s += 1
                elif A[i] > A[i-1]:
                    le = 1
                    s = 2
                else:
                    le = s = 0
            else:
                if A[i] < A[i-1]:
                    le = -1
                    s = 2
                elif A[i] > A[i-1]:
                    le = 1
                    s = 2
                else:
                    le = s = 0
            ret = max(ret, s)
        
        return ret