class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        M = 1000000000 + 7
        A.sort()
        n = len(A)
        ret = 0
        d = {}
        for i in A:
            d[i] = d.get(i, 0) + 1
        for i in range(n - 2):
            d[A[i]] -= 1
            j = i + 1
            k = n - 1
            x = target - A[i]
            y = A[j] + A[k]
            while j < k:
                if A[j] + A[k] < x:
                    j += 1
                elif A[j] + A[k] > x:
                    k -= 1
                else:
                    if A[j] == A[k]:
                        ret = (ret + (d[A[j]] * (d[A[j]] - 1)) // 2) % M
                    else:
                        ret = (ret + d[A[j]] * d[A[k]]) % M
                    i += d[A[j]]
                    k -= d[A[k]]
                    
        return ret
                
            
            
        
        