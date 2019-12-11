from heapq import heappush, heappop
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        x, y = min(A), max(A)
        if x == y:
            return 0
        A = list(set(A))
        A.sort()
        n = len(A)
        for i in range(n):
            A[i] = A[i] + K
        
        h = [-A[-1]]
        ret = A[-1] - A[0]
        x, y = A[0], A[-1]
        k2 = K * 2
        for i in range(n-1, 0, -1):
            t = A[i] - k2
            heappush(h, -t)
            heappush(h, -A[i-1])
            if -h[0]== A[i]:
                heappop(h)
            x = min(x, t)
            y = -h[0]
            ret = min(ret, abs(y-x))
        
        return ret