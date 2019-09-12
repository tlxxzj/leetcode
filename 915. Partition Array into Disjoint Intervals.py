class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        inf = float('inf')
        minx = [inf for i in range(n+1)]
        for i in range(n-1, -1, -1):
            minx[i] = min(A[i], minx[i+1])
        
        maxx = -inf
        for i in range(n):
            maxx = max(A[i], maxx)
            if maxx <= minx[i+1]:
                return i+1
        return n