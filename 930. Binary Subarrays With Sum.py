class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        ret = 0
        i, j = 0, 0
        s = 0
        while i < n and j < n:
            pre, post = 0, 0
            while i < n and A[i] == 0:
                pre += 1
                i += 1
            while j < n and s < S:
                s += A[j]
                j += 1
            while j < n and A[j] == 0:
                post += 1
                j += 1
            if s == S:
                print(i, j, pre, post)
                if s == 0:
                    ret += pre * (pre + 1) // 2
                else:
                    ret += (pre + 1) * (post + 1)
            if s > 0:
                s -= 1
            i += 1
        return ret
            
                
            